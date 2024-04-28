import sys
from scripts.load_persons import load_persons_from_json
from scripts.load_contacts import load_contacts_from_json
from connected_persons.connected_persons_by_job import get_connected_persons_by_job
from connected_persons.connected_persons_by_contact import get_connected_persons_by_contact

if(len(sys.argv) == 1):
  print('Missing person ID')
  exit()

person_id = int(sys.argv[1])
persons = load_persons_from_json('persons.json')
contacts = load_contacts_from_json('contacts.json')

connected_persons_by_job = get_connected_persons_by_job(persons, person_id)
connected_persons_by_contact = get_connected_persons_by_contact(persons, contacts, person_id)

for person_id in set(connected_persons_by_job).union(set(connected_persons_by_contact)):
  person = persons[person_id]
  print(person.id, ":", person.first, person.last)