"""
File: staff.py
Description: Defines the Staff class for zoo employees responsible for caring for animals and enclosures.
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Staff:
    def __init__(self, name, role=None):
        self.__name = name
        self.__role = role
        self.__assigned_animals = []
        self.__assigned_enclosures = []


    def get_name(self):
        return self.__name


    def get_role(self):
        return self.__role


    def set_name(self, value):
        if not value:
            raise ValueError("Staff name cannot be empty.")
        self.__name = str(value)


    def set_role(self, value):
        if not value:
            raise ValueError("Role cannot be empty.")
        self.__role = str(value).lower()


    name = property(get_name, set_name)
    role = property(get_role, set_role)

    def get_assigned_animals(self):
        return self.__assigned_animals

    def get_assigned_enclosures(self):
        return self.__assigned_enclosures


    assigned_animals = property(get_assigned_animals)
    assigned_enclosures = property(get_assigned_enclosures)

    def assign_animal(self, animal):
        if animal in self.__assigned_animals:
            raise ValueError("Animal already assigned.")
        self.__assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        if enclosure in self.__assigned_enclosures:
            raise ValueError("Enclosure already assigned.")
        self.__assigned_enclosures.append(enclosure)