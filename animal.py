"""
File: animal.py
Description: Base class for animals, including common traits and actions.
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod
from health_record import HealthRecord

class Animal(ABC):
    """Base class for all animals."""

    def __init__(self, name, species, age, diet):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__health_records = []

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_diet(self):
        return self.__diet

    def get_health_records(self):
        return self.__health_records

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

    def set_diet(self, value):
        if not value:
            raise ValueError("Diet cannot be empty.")
        self.__diet = str(value)

    name = property(get_name, set_name)
    species = property(get_species, set_species)
    age = property(get_age, set_age)
    diet = property(get_diet, set_diet)
    health_records = property(get_health_records)

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        return f"{self.__name} is eating."

    def sleep(self):
        return f"{self.__name} is sleeping."


    def add_health_record(self, record):
        if not isinstance(record, HealthRecord):
            raise ValueError("Record must be a HealthRecord.")
        self.__health_records.append(record)

    def is_under_treatment(self):
        return any(r.under_treatment for r in self.__health_records)

    def latest_health_summary(self):
        if not self.__health_records:
            return "No health records."
        r = self.__health_records[-1]
        status = "under treatment" if r.under_treatment else "resolved"
        parts = [
            f"{self.__name}: {r.issue}",
            f"severity: {r.severity}",
            f"date: {r.date}",
            status
        ]
        if r.treatment:
            parts.append(f"treatment: {r.treatment}")
        return " | ".join(parts)