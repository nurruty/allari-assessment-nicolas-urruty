from connected_persons.connected_persons_by_job import get_connected_persons_by_job
from connected_persons.connected_persons_by_contact import get_connected_persons_by_contact

def get_connected_persons(person_id, persons, contacts):
  if(person_id not in persons):
    exit("Person with ID %d not found" %person_id)
   
  connected_persons_by_job = get_connected_persons_by_job(persons, person_id)
  connected_persons_by_contact = get_connected_persons_by_contact(persons, contacts, person_id)

  connected_persons = set(connected_persons_by_job).union(set(connected_persons_by_contact))

  if not connected_persons:
      exit("No connected Persons to person ID: %d" %person_id)

  for person_id in connected_persons:
    person = persons[person_id]
    print("{}: {} {}".format(person.id,person.first, person.last))