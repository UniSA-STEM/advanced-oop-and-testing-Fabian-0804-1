"""
File: enclosure.py
Description: Represents a zoo enclosure that houses animals
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Enclosure:
    _ALLOWED_ENVIRONMENTS = ("savannah", "aquatic", "rainforest", "desert", "arctic", "grassland")

    def __init__(self, name, environment, capacity):
        self.__name = name
        self.__environment = environment
        self.__capacity = capacity

    def get_name(self):
        return self.__name

    def get_environment(self):
        return self.__environment

    def get_capacity(self):
        return self.__capacity

    def set_name(self, value):
        if not value:
            raise ValueError("Enclosure name cannot be empty.")
        self.__name = str(value)

    def set_environment(self, value):
        if not value or str(value).lower() not in self._ALLOWED_ENVIRONMENTS:
            raise ValueError(f"Environment must be one of: {', '.join(self._ALLOWED_ENVIRONMENTS)}.")
        self.__environment = str(value).lower()

    def set_capacity(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Capacity must be an integer of 1 or more.")
        self.__capacity = value

    name = property(get_name, set_name)
    environment = property(get_environment, set_environment)
    capacity = property(get_capacity, set_capacity)