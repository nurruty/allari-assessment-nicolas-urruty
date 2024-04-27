import json

class Phone:
    def __init__(self, number, type):
        self.number = number
        self.type = type

class Contact:
    def __init__(self, id, owner_id, contact_nickname, phones):
        self.id = id
        self.owner_id = owner_id
        self.contact_nickname = contact_nickname
        self.phones = phones

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

def normalize_phone(phone_number):
    # Remove non-digit characters and country code if present
    digits = ''.join(filter(str.isdigit, phone_number))
    if len(digits) == 11 and digits[0] == '1':
        digits = digits[1:]  # Remove country code '1'
    return digits
