# Write a Python program to test whether a number is within 100 of 1000 or 2000

def near_thousand(num):
    return ((abs(1000 - num) <= 100) or (abs(2000 - num) <= 100))

num = float(input('Enter a number: '))
res = near_thousand(num)
print(res)