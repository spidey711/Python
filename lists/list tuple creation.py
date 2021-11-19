#  Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

user_list = str(input("Enter comma separated values: ")).replace(',',"")
list1 = list(user_list)
tuple1 = tuple(user_list)
print(list1)
print(tuple1)