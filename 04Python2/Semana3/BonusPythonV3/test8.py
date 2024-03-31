class User:
    location = 'remote'
    def __init__(self, name):
        self.name = name
        self.id = 1234
    def debug(self):
        self.tracking = True
        