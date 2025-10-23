"""
File: animal.py
Description: Base class for animals, including common traits and actions.
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Animal:
    def __init__(self, name, species, age):
        self.__name = name
        self.__species = species
        self.__age = age

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def set_name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self.__name = str(value)

    def set_species(self, value):
        if not value:
            raise ValueError("Species cannot be empty.")
        self.__species = str(value)

    def set_age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.__age = value

    name = property(get_name, set_name)
    species = property(get_species, set_species)
    age = property(get_age, set_age)