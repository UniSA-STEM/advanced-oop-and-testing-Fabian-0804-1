"""
File: bird.py
Description: Represents a bird subclass of Animal
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, diet, can_fly=True):
        super().__init__(name, species, age, diet)
        self.__can_fly = can_fly

    def get_can_fly(self):
        return self.__can_fly

    def set_can_fly(self, value):
        if not isinstance(value, bool):
            raise ValueError("can_fly must be True or False.")
        self.__can_fly = value

    can_fly = property(get_can_fly, set_can_fly)

    def make_sound(self):
        return "Bird sound"