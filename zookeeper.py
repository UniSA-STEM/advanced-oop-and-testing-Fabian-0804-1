from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, role="zookeeper")

    def perform_duties(self):
        return "Feeds animals and cleans enclosures"