# Write a Python program to add two objects if both objects are an integer type
def typeCast(a, b):
    if type(a) == type(b):
        print(a + b)
    else:
        print("Different types detected")

     # If you want to test with string, do so with "Text" or 'Text' otherwise it will give an error
a = eval(input("Enter something: "))
b = eval(input("Enter something: "))
typeCast(a, b)