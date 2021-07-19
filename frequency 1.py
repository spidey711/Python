# Write a Python program to count the number 4 in a given list

def frequency(user_list):
    count = 0
    for number in user_list:
        if number == 4:
            count += 1
    print(count)

user_list = [1,4,2,3,4,5,3,4,5,6,6,7,8,8,4,5,4,3,4,2,1,1,5,6,3,2,4,5,3,4,5,6,7,5,4,3,7,9,0,7]
res = frequency(user_list)
print(res)