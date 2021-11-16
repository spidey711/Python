class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of {self.name} is {capacity} passengers."
    
bus = Vehicle('volvo',180,20)
print(bus.seating_capacity())