from parent import Human

class Wizard(Human):
    def __init__(self, tool, name, hp):
        super().__init__(name, hp)
        self.tool = tool

    def cast_spell(self, spell_name):
        return f"Casting {spell_name} and {self.defend()}  tool {self.tool}!"

wizard = Wizard("Magic Wand", "Gandalf", 100)
print(wizard.hp)