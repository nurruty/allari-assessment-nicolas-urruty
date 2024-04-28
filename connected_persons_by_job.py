from datetime import datetime

def overlaps_90_days(start1, end1, start2, end2):
    today = datetime.today().date()
    end_or_today1 = end1 or today
    end_or_today2 = end2 or today
         
    if(start1 <= end_or_today2 and end_or_today1 >= start2) or (start2 <= end_or_today1 and end_or_today2 >= start1):
        diff = 0
        # When one range contains another
        if(start1 <= start2) and (end_or_today1 >= end_or_today2):
            diff = end_or_today2 - start2
             
        # When one range is included in the other
        if(start2 <= start1) and (end_or_today1 <= end_or_today2):
            diff = end_or_today1 - start1

        # When ranges partially intercept - right
        if(start1 >= start2) and (end_or_today1 >= end_or_today2):
            diff = end_or_today2 - start1

        #When ranges partially intercept - left
        if(start1 <= start2) and (end_or_today1 <= end_or_today2):
            diff = end_or_today1 - start2
        
        return diff.days >= 90
    else:
        return False
    
def have_worked_together(first_person, second_person):
    for exp1 in first_person.experience:
        for exp2 in second_person.experience:
            if exp1.company == exp2.company and overlaps_90_days(exp1.start, exp1.end, exp2.start, exp2.end):
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

