# Write a Python program to concatenate all elements in a list into a string and return it

def string(user_list):
    new_list = ' '.join(user_list)
    print(new_list)

user_list = ['Hello','my','name','is','Spider','-','Man']
res = string(user_list)
print(res)