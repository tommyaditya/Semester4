class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "The car drives on the road."

class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is pedaled along the path."

class Boat(Vehicle):
    def move(self):
        return "The boat sails on the water."

vehicles = [Car(), Bicycle(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())