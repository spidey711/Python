# Write a Python program to display your details like name, age, address in three different lines

def details(name, age, address):
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

name = str(input("Enter name: "))
age = int(input("Enter number: "))
address = str(input("Enter address: "))
details(name, age, address)