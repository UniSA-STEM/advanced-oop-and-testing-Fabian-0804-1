"""
File: zoo.py
Description: Manages animals, enclosures, and staff; assignments, routines, and simple reports
Author: Fabian DiGrazia
ID: 110459219
Username: diyfy006
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Zoo:
    """Main class that manages animals, staff, and enclosures."""

    def __init__(self, name):
        self.__name = name
        self.__animals = []
        self.__enclosures = []
        self.__staff = []

    def get_name(self):
        return self.__name

    def get_animals(self):
        return self.__animals

    def get_enclosures(self):
        return self.__enclosures

    def get_staff(self):
        return self.__staff

    def set_name(self, value):
        if not value:
            raise ValueError("Zoo name cannot be empty.")
        self.__name = str(value)

    name = property(get_name, set_name)
    animals = property(get_animals)
    enclosures = property(get_enclosures)
    staff = property(get_staff)


    def add_animal(self, animal):
        if animal in self.__animals:
            raise ValueError("Animal already added.")
        self.__animals.append(animal)

    def remove_animal(self, animal):
        if animal not in self.__animals:
            raise ValueError("Animal not found.")
        self.__animals.remove(animal)

    def add_enclosure(self, enclosure):
        if enclosure in self.__enclosures:
            raise ValueError("Enclosure already added.")
        self.__enclosures.append(enclosure)

    def remove_enclosure(self, enclosure):
        if enclosure not in self.__enclosures:
            raise ValueError("Enclosure not found.")
        self.__enclosures.remove(enclosure)

    def add_staff(self, member):
        if member in self.__staff:
            raise ValueError("Staff already added.")
        self.__staff.append(member)

    def remove_staff(self, member):
        if member not in self.__staff:
            raise ValueError("Staff not found.")
        self.__staff.remove(member)


    def assign_animal_to_staff(self, animal, member):
        if animal not in self.__animals:
            raise ValueError("Animal must belong to the zoo.")
        if member not in self.__staff:
            raise ValueError("Staff must belong to the zoo.")
        member.assign_animal(animal)

    def assign_enclosure_to_staff(self, enclosure, member):
        if enclosure not in self.__enclosures:
            raise ValueError("Enclosure must belong to the zoo.")
        if member not in self.__staff:
            raise ValueError("Staff must belong to the zoo.")
        member.assign_enclosure(enclosure)

    def assign_animal_to_enclosure(self, animal, enclosure):
        if animal not in self.__animals:
            raise ValueError("Animal must belong to the zoo.")
        if enclosure not in self.__enclosures:
            raise ValueError("Enclosure must belong to the zoo.")
        enclosure.add_animal(animal)

    def daily_routine(self):
        logs = []
        for member in self.__staff:
            role = (member.role or "").lower()

            if role == "zookeeper":
                for a in member.assigned_animals:
                    logs.append(member.feed_animal(a))
                for e in member.assigned_enclosures:
                    logs.append(member.clean_enclosure(e))

            elif role == "veterinarian":
                for a in member.assigned_animals:
                    logs.append(member.conduct_health_check(a))

        return logs


    def report_animals_by_species(self):
        groups = {}
        for a in self.__animals:
            groups.setdefault(a.species, []).append(a.name)
        lines = []
        for species, names in sorted(groups.items()):
            lines.append(f"{species}: {', '.join(names)}")
        return "\n".join(lines) if lines else "No animals."

    def report_enclosure_statuses(self):
        if not self.__enclosures:
            return "No enclosures."
        return "\n".join(e.get_enclosure_status() for e in self.__enclosures)