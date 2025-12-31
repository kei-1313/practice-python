class Human:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def defend(self):
        return f"{self.name} is defending with {self.hp} HP."
