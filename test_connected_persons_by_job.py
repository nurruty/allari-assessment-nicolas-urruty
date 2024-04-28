import pytest
from datetime import datetime

from connected_persons_by_job import overlaps_90_days, have_worked_together, get_connected_persons_by_job
from load_persons import Person, Experience


@pytest.mark.parametrize("start1, end1, start2, end2, expected", [
    (datetime(2023, 1, 1).date(), datetime(2023, 10, 1).date(), datetime(2023, 2, 1).date(), datetime(2023, 5, 4).date(), True),  # Overlaps by more than 90 days
    (datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), datetime(2023, 3, 1).date(), datetime(2023, 3, 10).date(), False),  # Overlaps by less than 90 days
    (datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), datetime(2024, 5, 1).date(), datetime(2024, 6, 1).date(), False),  # No overlap
    (datetime(2023, 1, 1).date(), None, datetime(2023, 3, 1).date(), None, True),  # Overlaps by more than 90 days (still working)
    (datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), True),  # Same period
    (datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), datetime(2024, 1, 1).date(), datetime(2024, 12, 31).date(), False),  # No overlap, different years
    (datetime(2023, 1, 1).date(), datetime(2024, 4, 4).date(), datetime(2024, 1, 1).date(), datetime(2024, 4, 4).date(), True),  # Overlap starting in different years
])
def test_overlaps_90_days(start1, end1, start2, end2, expected):
    assert overlaps_90_days(start1, end1, start2, end2) == expected


def create_person(person_id, first, last, phone, experiences):
    return Person(person_id, first, last, phone, experiences)


@pytest.mark.parametrize("experiences1, experiences2, expected", [
    ([
        Experience("CompanyA", "The best company", datetime(2024, 1, 1).date(), datetime(2024, 4, 1).date())
    ], [
        Experience("CompanyA", "The best company", datetime(2024, 1, 1).date(), datetime(2024, 6, 1).date())
    ], True),  # Worked together with more than 90 days overlap
    ([
        Experience("CompanyA", "The best company", datetime(2024, 1, 1).date(), datetime(2024, 4, 1).date())
    ], [
        Experience("CompanyA", "The best company", datetime(2024, 3, 1).date(), None)
    ], False),  # Worked together with less than 90 days overlap
    ([
        Experience("CompanyA", "The best company", datetime(2024, 1, 1).date(), datetime(2024, 4, 1).date())
    ], [
        Experience("CompanyB", "The second best company", datetime(2024, 1, 1).date(), datetime(2024, 6, 1).date())
    ], False),  # No overlap in experiences
    ([
        Experience("CompanyA", "The best company", datetime(2023, 1, 1).date(), None)
    ], [
        Experience("CompanyA", "The best company", datetime(2023, 3, 1).date(), None)
    ], True),  # Worked together with open end date
])
def test_have_worked_together(experiences1, experiences2, expected):
    person1 = create_person(1, 'Steve', 'Jobs', '123456789', experiences1)
    person2 = create_person(2, 'Bill', 'Gates', '987654321', experiences2)
    assert have_worked_together(person1, person2) == expected


@pytest.fixture
def persons():
    # Sample persons data for testing
    return {
        1: Person(1, 'Steve', 'Jobs', '123456789', [
            Experience("CompanyA", "The best company", datetime(2024, 1, 1).date(), datetime(2024, 4, 1).date())
        ]),
        2: Person(2, 'Bill', 'Gates', '987654321', [
            Experience("CompanyA", "The best company", datetime(2024, 1, 1).date(), datetime(2024, 6, 1).date())
        ]),
        3: Person(3, 'Jeff', 'Bezos', '555555555', [
            Experience("CompanyB", "The second best company", datetime(2024, 1, 1).date(), None)
        ]),
        4: Person(4, 'Elon', 'Musk', '111111111', [
            Experience("CompanyB", "The second best company", datetime(2024, 1, 1).date(), datetime(2024, 2, 1).date()),
            Experience("CompanyA", "The best company", datetime(2023, 12, 1).date(), datetime(2024, 5, 1).date())
        ]),
        5: Person(5, 'Mark', 'Zuckerberg', '222222222', [
            Experience("CompanyB", "The second best company", datetime(2023, 10, 1).date(), datetime(2024, 4, 1).date())
        ]),
         6: Person(6, 'Larry', 'Page', '333333333', [
            Experience("CompanyC", "", datetime(2024, 4, 1).date(), None)
        ]),
    }

@pytest.mark.parametrize("person_id, expected", [
    (1, [2,4]),
    (2, [1, 4]),
    (3, [5]),
    (4, [1, 2]),
    (5, [3]),
    (6, [])
])
def test_get_connected_persons_by_job_person_exists(persons, person_id, expected):
    connected_ids = get_connected_persons_by_job(persons, person_id)
    assert connected_ids == expected

def test_get_connected_persons_by_job_person_does_not_exist(persons):
    with pytest.raises(Exception):
        get_connected_persons_by_job(persons, 7)