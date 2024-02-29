class User:
    def __init__(self, id):
        self.id = id

class Employee(User):
    def __init__(self, id, name):
        self.id = id
        self.name = name