import json
from datetime import datetime
from classes.person import Person, Experience
from utils.utils import normalize_phone

def load_persons_from_json(file_path):
    persons = dict()
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            id = item.get('id')
            first = item.get('first')
            last = item.get('last')
            phone = item.get('phone')
            phone = None if phone is None else normalize_phone(phone)
            experience_list = []
            for exp in item.get('experience', []):
                company = exp.get('company')
                title = exp.get('title')
                start = datetime.strptime(exp.get('start'), "%Y-%m-%d").date()
                end = datetime.strptime(exp.get('end'), "%Y-%m-%d").date() if exp.get('end') else None
                experience = Experience(company, title, start, end)
                experience_list.append(experience)
            person = Person(id, first, last, phone, experience_list)
            persons[person.id] = (person)
    return persons