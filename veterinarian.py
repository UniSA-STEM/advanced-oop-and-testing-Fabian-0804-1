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
    def __init__(self, name):
        super().__init__(name, role="veterinarian")

    def perform_duties(self):
        return "Conducts health checks and updates records"