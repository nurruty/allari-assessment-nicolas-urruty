from utils.utils import overlaps_days
    
def have_worked_together(first_person, second_person):
    for exp1 in first_person.experience:
        for exp2 in second_person.experience:
            if exp1.company == exp2.company and overlaps_days(exp1.start, exp1.end, exp2.start, exp2.end, 90):
                return True
    return False

def get_connected_persons_by_job(persons, person_id):
    connectedIds = []
    
    if(person_id not in persons):
        raise Exception('Error: Person with ID not found')

    target_person = persons[person_id]
    
    for key in persons:
        if(key != person_id):
          person = persons[key]
          if(target_person != None) and have_worked_together(person, target_person):
            connectedIds.append(person.id)

    return connectedIds

