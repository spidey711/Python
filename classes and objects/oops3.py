# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.
class Vehicle:
    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage
    
class Bus(Vehicle):
    def getDetails(self):
        return f"Name:{self.name}\nMax Speed:{self.maxSpeed}\nMileage:{self.mileage}"

bus = Bus('Toyota',180,20)
print(bus.getDetails())