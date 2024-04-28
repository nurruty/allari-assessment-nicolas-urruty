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