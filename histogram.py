# Write a Python program to create a histogram from a given list of integers

def histogram(data):
    for item in data:
        print('.' * item)

data = []
num_data = int(input("Enter number of entries: "))
for item in range(0, num_data):
    user_input = int(input())
    data.append(user_input)

res = histogram(data)
print(res)