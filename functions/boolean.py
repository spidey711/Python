# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def check_bool(num1, num2):
    if num1 == num2 or (num1 + num2) == 5 or (num1 - num2) == 5:
        print(True)
    else:
        print(False)

num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
check_bool(num1, num2)