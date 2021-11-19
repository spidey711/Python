# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

def subtract(num):
    if num <= 17:
        return num-17
    else:
        return (num-17)*2

num = float(input("Enter a number: "))
res = subtract(num)
print(res)