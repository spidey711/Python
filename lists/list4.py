'''
Concatenate two lists in the following order:-
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''
res = []
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
    for j in list2:
        res.append(f"{i}{j}")
print(res)
