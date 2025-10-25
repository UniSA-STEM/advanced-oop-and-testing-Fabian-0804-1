"""
File: reptile.py
Description: Represents a reptile subclass of Animal
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Reptile(Animal):
    def __init__(self, name, species, age, diet, is_venomous=False):
        super().__init__(name, species, age, diet)
        self.__is_venomous = is_venomous

        def get_is_venomous(self):
            return self.__is_venomous

        def set_is_venomous(self, value):
            if not isinstance(value, bool):
                raise ValueError("is_venomous must be True or False.")
            self.__is_venomous = value

        is_venomous = property(get_is_venomous, set_is_venomous)

    def make_sound(self):
        return "Reptile sound"