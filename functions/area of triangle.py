# Write a Python program that will accept the base and height of a triangle and compute the area

def area(height, base):
    print((height*base)/2)

base = float(input("Enter base value: "))
height = float(input("Enter height: "))
res = area(height, base)
print(res)