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