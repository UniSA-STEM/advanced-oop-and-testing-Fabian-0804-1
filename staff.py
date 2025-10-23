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