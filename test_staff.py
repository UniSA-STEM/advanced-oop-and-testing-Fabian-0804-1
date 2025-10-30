"""
File: test_staff.py
Description: Tests for Staff and subclasses (Zookeeper, Veterinarian)
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from zookeeper import Zookeeper
from veterinarian import Veterinarian
from mammal import Mammal
from enclosure import Enclosure

def test_zookeeper_duties():
    keeper = Zookeeper("Sam")
    animal = Mammal("Leo", "Lion", 4, "Carnivore")
    enclosure = Enclosure("Savannah", "Grassland", 2, "Large")

    result_feed = keeper.feed_animal(animal)
    result_clean = keeper.clean_enclosure(enclosure)

    assert "feeds" in result_feed.lower()
    assert "cleans" in result_clean.lower()

def test_veterinarian_health_check():
    vet = Veterinarian("Dr Lee")
    animal = Mammal("Leo", "Lion", 4, "Carnivore")
    result = vet.conduct_health_check(animal)

    assert "health" in result.lower()