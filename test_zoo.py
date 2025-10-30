"""
File: test_zoo.py
Description: Tests for Zoo class and overall integration
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from zoo import Zoo
from mammal import Mammal
from bird import Bird
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian

def test_add_and_assignments():
    zoo = Zoo("City Zoo")
    lion = Mammal("Leo", "Lion", 5, "Carnivore")
    bird = Bird("Tweety", "Canary", 2, "Herbivore")
    enc1 = Enclosure("Savannah", "Grassland", 3, "Large")
    keeper = Zookeeper("Sam")
    vet = Veterinarian("Dr Lee")

    zoo.add_animal(lion)
    zoo.add_animal(bird)
    zoo.add_enclosure(enc1)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    assert lion in zoo.animals
    assert enc1 in zoo.enclosures
    assert keeper in zoo.staff

def test_daily_routine_logs():
    zoo = Zoo("City Zoo")
    keeper = Zookeeper("Sam")
    lion = Mammal("Leo", "Lion", 5, "Carnivore")
    enc1 = Enclosure("Savannah", "Grassland", 2, "Large")

    zoo.add_staff(keeper)
    zoo.add_animal(lion)
    zoo.add_enclosure(enc1)
    zoo.assign_animal_to_staff(lion, keeper)
    zoo.assign_enclosure_to_staff(enc1, keeper)

    logs = zoo.daily_routine()
    assert any("feeds" in log.lower() for log in logs)
    assert any("cleans" in log.lower() for log in logs)