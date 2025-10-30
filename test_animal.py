"""
File: test_animal.py
Description: Tests for Animal subclasses (Mammal, Bird, Reptile)
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from mammal import Mammal
from bird import Bird
from reptile import Reptile

def test_make_sound():
    mammal = Mammal("Leo", "Lion", 5, "Carnivore")
    bird = Bird("Tweety", "Canary", 2, "Herbivore")
    reptile = Reptile("Rex", "Snake", 3, "Carnivore")

    assert mammal.make_sound() == "Mammal sound"
    assert bird.make_sound() == "Bird sound"
    assert reptile.make_sound() == "Reptile sound"

def test_unique_traits():
    mammal = Mammal("Leo", "Lion", 5, "Carnivore", has_fur=True)
    bird = Bird("Tweety", "Canary", 2, "Herbivore", can_fly=True)
    reptile = Reptile("Rex", "Snake", 3, "Carnivore", is_venomous=True)

    assert mammal.has_fur is True
    assert bird.can_fly is True
    assert reptile.is_venomous is True