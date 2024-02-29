class User:
    def __init__(self, name):
        self.name = name

user1 = User("brandom")
user2 = User("Devi")

print(isinstance(user1, object))
print(isinstance(user2, type))
