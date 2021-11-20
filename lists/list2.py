'''
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
res = []
for i in range(len(list1)):
    for j in range(len(list2)):
        a = i = j
        res.append(f"{list1[a]}{list2[a]}")
    break
print(res)