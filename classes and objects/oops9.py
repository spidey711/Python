'''
Follow the steps:

    Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the __init__()method.
    Create a variable named number_of_sides and set it equal to 3.
    Create a method named check_angles. The sum of a triangle's three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
    Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
    Print out my_triangle.number_of_sides and print out my_triangle.check_angles().

'''

class Triangle:
    num_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def checkAngles(self):
        if self.angle1+self.angle2+self.angle3 == 180:
            return True
        else:
            return False
my_triangle = Triangle(90, 30, 60)
print(my_triangle.num_sides)
print(my_triangle.checkAngles())