from animal import Animal

class Reptile(Animal):
    def __init__(self, name, species, age):
        super().__init__(name, species, age)

    def make_sound(self):
        return "Reptile sound"