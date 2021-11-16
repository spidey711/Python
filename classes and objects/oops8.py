# Exercise 8: Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    
class Bus(Vehicle):
    pass

School_Bus = Vehicle('volvo', 20, 50)
print(isinstance(School_Bus, Vehicle)) # takes obj, class and returns True/False