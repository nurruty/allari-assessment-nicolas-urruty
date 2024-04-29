import sys
from scripts.load_persons import load_persons_from_json
from scripts.load_contacts import load_contacts_from_json
from connected_persons.connected_persons import get_connected_persons


if(len(sys.argv) == 1):
  exit("Missing person ID")

persons = load_persons_from_json('persons.json')
contacts = load_contacts_from_json('contacts.json')
person_id = int(sys.argv[1])
get_connected_persons(person_id, persons, contacts)
