class User:
    type = "guest"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.type}."



user1 = User("Alice", 30)
print(user1.greet())

user2 = User("Bob", 25)
print(user2.greet())

User.type = "admin"

print(user1.greet())
print(user2.greet())