# NINJA BONUS: Use modules to separate out the classes into different files.

import pets

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()


Alan_dog = pets.Pets("Kevin", "dog", "dig holes")
Alan = Ninja("Alan", "Walker", Alan_dog, "dog biscuit", "dog food")

Alan.walk().feed().bathe()
print(Alan_dog.energy, Alan_dog.health)