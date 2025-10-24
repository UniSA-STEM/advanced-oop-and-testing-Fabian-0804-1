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

    def perform_duties(self):
        return "Feeds animals and cleans enclosures"