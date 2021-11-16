# Write a program to create a function that takes two arguments, name and age, and print their value.
def func(name, age):
    return name, age

name = str(input("Enter name: "))
age = int(input("Enter age: "))
print(func(name, age))