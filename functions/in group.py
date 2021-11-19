# Write a Python program to check whether a specified value is contained in a group of values
 
def group(num):
    given_list = [1,5,6,4,3,6,7,4,3,6,766,4,3,56456,4,5,4,32,324,3536,363,6336,576,3635,536,3,5]
    return num in given_list

num = int(input("Enter number: "))
res = group(num)
print(res)