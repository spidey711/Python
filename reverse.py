# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

first = str(input("Enter first name: "))
last = str(input("Enter last name: "))
result = first[::-1] + " " + last[::-1]
print(result)