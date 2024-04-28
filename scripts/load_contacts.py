import json
from classes.contact import Contact, Phone
from utils.utils import normalize_phone

def load_contacts_from_json(file_path):
    contacts = []
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            id = item.get('id')
            owner_id = item.get('owner_id')
            contact_nickname = item.get('contact_nickname')
            phones = []
            for phone_data in item.get('phone', []):
                number = normalize_phone(phone_data.get('number'))
                type = phone_data.get('type')
                phone = Phone(number, type)
                phones.append(phone)
            contact = Contact(id, owner_id, contact_nickname, phones)
            contacts.append(contact)
    return contacts

