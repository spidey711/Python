# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2

def string_multiply(user_str, num):
    if len(user_str) > 2:
       print(user_str[:2] * num)
    else:
        print(user_str * num)

user_str = str(input("Enter a sentence: "))
num = int(input("How many copies? "))
res = string_multiply(user_str, num)
print(res)