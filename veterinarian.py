"""
File: veterinarian.py
Description: Represents a veterinarian subclass of Staff
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff

class Veterinarian(Staff):
    """Veterinarian responsible for animal health."""

    def __init__(self, name):
        super().__init__(name, role="veterinarian")

    def feed_animal(self, animal):
        return f"Veterinarian {self.name} assists feeding {animal.name} if needed."

    def clean_enclosure(self, enclosure):
        return f"Veterinarian {self.name} is not responsible for cleaning but may assist if required."

    def conduct_health_check(self, animal):
        return f"Veterinarian {self.name} performs a health check on {animal.name}."