# Exercise 7: Check type of an object

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
class Bus(Vehicle):
    pass
    
School_Bus = Bus('School Bus', 20, 50)
print(type(School_Bus))