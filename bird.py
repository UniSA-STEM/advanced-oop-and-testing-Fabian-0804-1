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
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)

    def make_sound(self):
        return "Bird sound"