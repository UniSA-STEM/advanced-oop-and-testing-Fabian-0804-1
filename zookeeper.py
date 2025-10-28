"""
File: zookeeper.py
Description: Represents a zookeeper subclass of Staff
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, role="zookeeper")

    def feed_animal(self, animal):
        return f"Zookeeper {self.name} feeds {animal.name}."

    def clean_enclosure(self, enclosure):
        return f"Zookeeper {self.name} cleans {enclosure.name}."

    def conduct_health_check(self, animal):
        return f"Zookeeper {self.name} observes {animal.name} and reports to the veterinarian."