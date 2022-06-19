# class Pets:

#     energy = 0
#     health = 0

#     def __init__(self, name, type, tricks):
#         self.name = name
#         self.type = pets_type
#         self.tricks = tricks
        
#     def sleep(self):
#         energy += 25

#     def eat(self):
#         energy += 5
#         health += 10
    
#     def play(self):
#         health += 5

#     def noise(self):
#         if self.type = "cat":
#             print("Miaow")
#         elif self.type = "dog":
#             print("Woof Woof")


# class Ninja(Pets):
#     def __init__(self, first_name, last_name, pet, treats, pet_food):
#         self.first_name = first_name
#         self.last_name = last_name
#         super().__init__(type)
#         self.treats = treats
#         self.pet_food = pet_food

#     def walk(self):
#         super().play()

#     def feed(self):
#         super().eat

#     def bathe(self):
#         super().noise()








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
        


Alan_dog = Pets("Kevin", "dog", "dig holes")
Alan = Ninja("Alan", "Walker", Alan_dog, "dog biscuit", "dog food")

Alan.walk().feed().bathe()
print(Alan_dog.energy, Alan_dog.health)


