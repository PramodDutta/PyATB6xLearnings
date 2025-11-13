class Dog:
    # Attributes - Instance variables | Data variables
    name = None
    breed = None
    height = None
    weight = None
    race = None

    def __init__(self, nameGiven, breedGiven):
        print("Param C")
        self.name = nameGiven
        self.breed = breedGiven

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleep -> " + self.name)

    def talk(self):
        pass


chow = Dog("chow", "mastiff")
rancho = Dog("rancho", "desi")

chow.sleep()
rancho.sleep()