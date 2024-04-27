from load_contacts import normalize_phone

def get_phones_by_person(persons, contacts):
    contact_phones_by_person = dict()

    for person_id in persons:
        person = persons[person_id]
        for contact in contacts:
            if(contact.owner_id == person.id):
                contact_phones_by_person[person.id] = (person.phone, [phone.number for phone in contact.phones])

    return contact_phones_by_person

def has_phone_in_contacts(phone, contact_phones):
    return phone in contact_phones

def get_connected_persons_by_contact(persons, contacts, person_id):
    contact_phones_by_person = get_phones_by_person(persons, contacts)
    connected_ids = []
    
    if person_id not in contact_phones_by_person:
        return []
    
    person_contact_phones = contact_phones_by_person[person_id][1]
    person_phone_number = normalize_phone(contact_phones_by_person[person_id][0])

       
    for target_id in contact_phones_by_person:
        if (target_id != person_id and target_id in contact_phones_by_person ):
            target_contact_phones = contact_phones_by_person[target_id][1]
            target_phone_number = normalize_phone(contact_phones_by_person[target_id][0])
            if has_phone_in_contacts(person_phone_number, target_contact_phones) or has_phone_in_contacts(target_phone_number, person_contact_phones):
                connected_ids.append(target_id)


    
    return connected_ids