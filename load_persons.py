import json
from datetime import datetime

class Experience:
    def __init__(self, company, title, start, end):
        self.company = company
        self.title = title
        self.start = start
        self.end = end

class Person:
    def __init__(self, id, first, last, phone, experience):
        self.id = id
        self.first = first
        self.last = last
        self.phone = phone
        self.experience = experience

def load_persons_from_json(file_path):
    persons = dict()
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            id = item.get('id')
            first = item.get('first')
            last = item.get('last')
            phone = item.get('phone')
            if phone is not None and '-' not in phone:
                phone = phone[:1] + '-' + phone[1:5] + '-' + phone[5:]  # Add dash if missing
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