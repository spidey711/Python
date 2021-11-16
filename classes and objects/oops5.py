#  Exercise 5: Define a property that must have the same value for every class instance (object)

# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
class Vehicle:

    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage
        self.color = 'white'
        
    def getDetails(self):
        return f"Color:{self.color}, Vehicle Name:{self.name}, Speed:{self.maxSpeed}, Mileage:{self.mileage}"
    
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass

bus = Bus('volvo',180,20)
# bus.color = 'Red'
car = Car('aston martin',260,30)
print(bus.getDetails())
print(car.getDetails())