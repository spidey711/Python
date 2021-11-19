# perform a linear search return index of target from the list

def linearsearch(given_list, target):
    for items in range(len(given_list)):
        if given_list[items] == target:
            print(items)
        else:
            pass

elements = input("Enter elements: ").split(",")
list1 = list(elements)
target = input("Enter target: ")
linearsearch(list1, target)