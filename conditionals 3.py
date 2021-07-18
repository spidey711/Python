# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum

def sum(num1, num2, num3):
    if num1 == num2 == num3:
        return(num1 + num2 + num3)*3
    else:
        return num1 + num2 + num3


num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))

res = sum(num1, num2, num3)
print(res)