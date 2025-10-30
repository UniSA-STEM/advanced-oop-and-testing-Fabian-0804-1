"""
File: test_enclosure.py
Description: Tests for Enclosure class
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure
from mammal import Mammal

def test_add_and_list_animals():
    enclosure = Enclosure("Savannah", "Grassland", 2, "Large")
    lion = Mammal("Leo", "Lion", 4, "Carnivore")
    enclosure.add_animal(lion)

    assert lion in enclosure.animals
    names = enclosure.list_animal_names()
    assert "Leo" in names

def test_clean_enclosure():
    enclosure = Enclosure("Savannah", "Grassland", 2, "Large")
    enclosure.clean = False
    enclosure.clean_enclosure()
    assert enclosure.clean is True