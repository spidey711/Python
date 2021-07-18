# Write a Python program to get a string which is n (non-negative integer) copies of a given string

def str_multiply(user_str, num_copy):
    print(user_str*num_copy)

user_str = str(input("Sentence: "))
num_copy  = int(input("How many times? "))

res = str_multiply(user_str, num_copy)
print(res)