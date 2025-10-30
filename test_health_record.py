"""
File: test_health_record.py
Description: Tests for HealthRecord and Animal health integration
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from mammal import Mammal
from health_record import HealthRecord

def test_health_record_creation():
    record = HealthRecord("Leg injury", "High", "2025-10-30", "Antibiotics", True, "Limping")
    assert record.issue == "Leg injury"
    assert record.under_treatment is True

def test_animal_under_treatment_block():
    lion = Mammal("Leo", "Lion", 5, "Carnivore")
    record = HealthRecord("Leg injury", "High", "2025-10-30", "Antibiotics", True)
    lion.add_health_record(record)
    assert lion.is_under_treatment() is True