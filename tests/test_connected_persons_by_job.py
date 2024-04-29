import pytest
from datetime import datetime

from connected_persons.connected_persons_by_job import have_worked_together, get_connected_persons_by_job
from classes.person import Person, Experience


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
    person1 = Person(1, 'Steve', 'Jobs', '123456789', experiences1)
    person2 = Person(2, 'Bill', 'Gates', '987654321', experiences2)
    assert have_worked_together(person1, person2) == expected


@pytest.fixture
def persons():
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
    with pytest.raises(Exception) as exception:
        get_connected_persons_by_job(persons, 7)
    assert str(exception.value) == 'Person with ID 7 not found'
    