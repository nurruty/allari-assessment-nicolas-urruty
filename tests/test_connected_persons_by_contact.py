import pytest

from classes.person import Person
from classes.contact import Contact, Phone
from connected_persons.connected_persons_by_contact import get_contacts_by_person, get_connected_persons_by_contact

@pytest.fixture
def persons():
    # Sample persons data for testing
    return {
        1: Person(1, 'Steve', 'Jobs', '0800111111', []),
        2: Person(2, 'Bill', 'Gates', '+1034589741', []),
        3: Person(3, 'Jeff', 'Bezos', '(020) 555555555', [])
    }

@pytest.fixture
def contacts():
    # Sample contacts data for testing
    return [
        Contact(1, 1, "Bill", [
            Phone("1034589741", "landline"),
            Phone("1234567890", "cell")
        ]),
        Contact(2, 2, "Jeff", [
            Phone("555555555", "landline"),
        ]),
        Contact(3, 3, "Steve", [
            Phone("0800111111", "landline")
        ])
    ]

def test_get_contacts_by_person(persons, contacts):
    expected_result = {
        1: (persons[1].phone, ["1034589741", "1234567890"]),
        2: (persons[2].phone, ["555555555"]),
        3: (persons[3].phone, ["0800111111"])
    }
    assert get_contacts_by_person(persons, contacts) == expected_result

def test_get_contacts_by_person_no_contacts(persons, contacts):
    expected_result = {
        1: (persons[1].phone, []),
        2: (persons[2].phone, ["555555555"]),
        3: (persons[3].phone, ["0800111111"])
    }
    assert get_contacts_by_person(persons, contacts[1:]) == expected_result


# get_connected_persons_by_contact
@pytest.mark.parametrize("person_id, expected", [
    (1, [2,3]),
    (2, [1]),
    (3, [1]),
])
def test_get_connected_persons_by_contact(persons, contacts, person_id, expected):
    assert get_connected_persons_by_contact(persons, contacts, person_id) == expected

def test_get_connected_persons_by_contact_person_not_found(persons, contacts):
    with pytest.raises(Exception):
        get_connected_persons_by_contact(persons, contacts, 4)

