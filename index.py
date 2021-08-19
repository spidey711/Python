# Return the index values of items in an iterable

def index(iterable):
    for items in range(len(iterable)):
        print("Index: {a} | Value: {b}".format(a=items, b=iterable[items]))
    
elements = input("Enter elements: ").split(",")
list1 = list(elements)
index(list1)