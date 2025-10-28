"""
File: mammal.py
Description: Represents a mammal subclass of Animal
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, age, diet, has_fur=True):
        super().__init__(name, species, age, diet)
        self.__has_fur = has_fur


    def get_has_fur(self):
        return self.__has_fur

    def set_has_fur(self, value):
        if not isinstance(value, bool):
            raise ValueError("has_fur must be True or False.")
        self.__has_fur = value

    has_fur = property(get_has_fur, set_has_fur)

    def make_sound(self):
        return "Mammal sound"
