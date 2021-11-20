# Given a list of numbers. write a program to turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]
res = []
for i in numbers:
    res.append(i**2)
print(res)