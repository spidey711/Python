# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user

def even_odd(num):
    if num % 2 == 0:
        print("{} is an even number".format(num))
    else:
        print("{} is an odd number".format(num))

num = float(input("Enter a number: "))
res = even_odd(num)
print(res)