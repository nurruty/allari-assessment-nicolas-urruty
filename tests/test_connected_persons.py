import pytest
import io
import sys
from connected_persons.connected_persons import get_connected_persons
from scripts.load_persons import load_persons_from_json
from scripts.load_contacts import load_contacts_from_json

@pytest.mark.parametrize("person_id, expected", [
    (0, """1: Steve Jobs
2: Bill Gates"""),
     (1, """0: Jane Doe
3: Tim Cook
4: Alan Turing"""),
     (2, """0: Jane Doe
3: Tim Cook
4: Alan Turing"""),
     (3, """1: Steve Jobs
2: Bill Gates
4: Alan Turing"""),
     (4, """1: Steve Jobs
2: Bill Gates
3: Tim Cook""")
])
def test_get_connected_persons(person_id, expected):
    persons = load_persons_from_json('tests/test_persons.json')
    contacts = load_contacts_from_json('tests/test_contacts.json')

    captured_output = io.StringIO()
    sys.stdout = captured_output

    get_connected_persons(person_id, persons, contacts)

    printed_output = captured_output.getvalue().strip()
    sys.stdout = sys.__stdout__

    assert printed_output == expected

@pytest.mark.parametrize("person_id, expected", [
    (5, "No connected Persons to person ID: 5")
])
def test_get_no_connected_persons(person_id, expected):
    persons = load_persons_from_json('persons.json')
    contacts = load_contacts_from_json('contacts.json')

    with pytest.raises(SystemExit) as exception:
      get_connected_persons(person_id, persons, contacts)
    assert str(exception.value) == expected



