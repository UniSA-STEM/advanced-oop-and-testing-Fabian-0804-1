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
        self.__animals = []
        self.__current_species = None

    def get_name(self):
        return self.__name

    def get_environment(self):
        return self.__environment

    def get_capacity(self):
        return self.__capacity

    def get_animals(self):
        return self.__animals

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
    animals = property(get_animals)


    def add_animal(self, animal):
        if len(self.__animals) >= self.__capacity:
            raise ValueError("Enclosure is at capacity.")
        if self.__current_species is None:
            self.__current_species = animal.species
        if animal.species != self.__current_species:
            raise ValueError("Incompatible species for this enclosure.")
        if animal in self.__animals:
            raise ValueError("Animal is already in this enclosure.")
        self.__animals.append(animal)

    def remove_animal(self, animal):
        if animal not in self.__animals:
            raise ValueError("Animal not found in this enclosure.")
        self.__animals.remove(animal)
        if not self.__animals:
            self.__current_species = None

    def list_animal_names(self):
        return [a.name for a in self.__animals]

    def get_enclosure_status(self):
        occupants = ", ".join(self.list_animal_names()) or "none"
        return (f"Enclosure: {self.__name} | Environment: {self.__environment} | "
                f"Capacity: {len(self.__animals)}/{self.__capacity} | "
                f"Species: {self.__current_species or 'unset'} | Animals: {occupants}")