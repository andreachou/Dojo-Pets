# NINJA BONUS: Use modules to separate out the classes into different files.

class Pets:

    # energy = 0
    # health = 0

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
        
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self

    def noise(self):
        if self.type == "cat":
            print("Miaow")
        elif self.type == "dog":
            print("Woof Woof")

