from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    age: int
    description: str
    hobbies: list[str] = field(default_factory=lambda: ["tennis", "baseball"])

user1 = User(name="Alice", age=30, description="A software developer from NY.")
user1.name = "Ivy"

print(user1.name)
print(user1.hobbies)

# 以下と同じ
# class User:
#     def __init__(self, name: str, age: int, description: str):
#         self.name = name
#         self.age = age
#         self.description = description