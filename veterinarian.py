from staff import Staff

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, role="veterinarian")

    def perform_duties(self):
        return "Conducts health checks and updates records"