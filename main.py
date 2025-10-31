"""
File: main.py
Description: Demonstrates the Zoo Management System by creating and managing animals, staff, and enclosures.
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from zoo import Zoo
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from health_record import HealthRecord


def print_header(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)



# 1) Create world: zoo, staff, enclosures, animals

def section_1_create():
    print_header("1) Create zoo, staff, enclosures, animals")

    zoo = Zoo("City Zoo")

    # staff
    keeper = Zookeeper("Sam")
    vet = Veterinarian("Dr Lee")
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # enclosures
    savannah = Enclosure("Savannah 1", "savannah", capacity=3, size="large", clean=True)
    rainforest = Enclosure("Rainforest Habitat", "rainforest", capacity=5, size="medium", clean=False)
    zoo.add_enclosure(savannah)
    zoo.add_enclosure(rainforest)

    # animals
    leo = Mammal("Leo", "Lion", 5, "Carnivore", has_fur=True)
    polly = Bird("Polly", "Parrot", 2, "Herbivore", can_fly=True)
    viper = Reptile("Viper", "Snake", 3, "Carnivore", is_venomous=True)
    zoo.add_animal(leo)
    zoo.add_animal(polly)
    zoo.add_animal(viper)

    print("Created zoo with 2 enclosures, 2 staff, 3 animals.")
    return zoo, keeper, vet, savannah, rainforest, leo, polly, viper



# 2) Animal behaviour

def section_2_animal_behaviour(leo, polly, viper):
    print_header("2) Animal behaviour")
    for a in (leo, polly, viper):
        print(f"{a.name} says:", a.make_sound())
        print(a.eat())
        print(a.sleep())



# 3) Enclosures: add animals, list occupants, cleanliness

def section_3_enclosures(zoo, savannah, rainforest, leo, polly):
    print_header("3) Enclosures: add animals, list occupants, cleanliness")

    # place animals
    zoo.assign_animal_to_enclosure(leo, savannah)
    zoo.assign_animal_to_enclosure(polly, rainforest)

    print("Savannah animals:", ", ".join(savannah.list_animal_names()))
    print("Rainforest animals:", ", ".join(rainforest.list_animal_names()))

    # Print enclosure info
    print(f"Rainforest status before cleaning: Size={rainforest.size}, "
          f"Clean={rainforest.clean}, Capacity={len(rainforest.animals)}/{rainforest.capacity}")

    print("Cleaner action:", rainforest.clean_enclosure())

    print(f"Rainforest status after cleaning: Size={rainforest.size}, "
          f"Clean={rainforest.clean}, Capacity={len(rainforest.animals)}/{rainforest.capacity}")



# 4) Staff roles & assignments

def section_4_staff_assign(zoo, keeper, vet, savannah, leo):
    print_header("4) Staff roles & assignments")
    zoo.assign_animal_to_staff(leo, keeper)
    zoo.assign_enclosure_to_staff(savannah, keeper)
    zoo.assign_animal_to_staff(leo, vet)
    print("Assignments: keeper -> (Leo, Savannah 1); vet -> (Leo).")



# 5) Health records & movement restriction

def section_5_health_and_restriction(zoo, leo, rainforest):
    print_header("5) Health records & movement restriction")

    record = HealthRecord(
        issue="Leg injury",
        severity="High",
        date="30-10-2025",
        treatment="Anti-inflammatory",
        under_treatment=True,
        notes="Limping"
    )
    leo.add_health_record(record)
    print("Latest health:", leo.latest_health_summary())

    print("Attempting to move Leo to Rainforest Habitat (should be blocked):")
    try:
        zoo.assign_animal_to_enclosure(leo, rainforest)
    except ValueError as e:
        print("Blocked as expected ->", e)



# 6) Daily routine & reports

def section_6_routine_and_reports(zoo):
    print_header("6) Daily routine & reports")

    logs = zoo.daily_routine()
    for line in logs:
        print(line)

    print("\nAnimals by species:")
    print(zoo.report_animals_by_species())

    print("\nEnclosure statuses:")
    print(zoo.report_enclosure_statuses())



if __name__ == "__main__":
    zoo, keeper, vet, savannah, rainforest, leo, polly, viper = section_1_create()
    section_2_animal_behaviour(leo, polly, viper)
    section_3_enclosures(zoo, savannah, rainforest, leo, polly)
    section_4_staff_assign(zoo, keeper, vet, savannah, leo)
    section_5_health_and_restriction(zoo, leo, rainforest)
    section_6_routine_and_reports(zoo)