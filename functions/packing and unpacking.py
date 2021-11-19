# Packing 
# Used when we dont know how many arguments we must give to a function
def func(*args):
    return sum(args)
print(func(1,2,2,3,3,4,4,4,5))
# We can give as many arguments as we want
# OUTPUT : 28

# Unpacking
# Used when we want to pass a mutable iterable as an argument
# *<iterable name>
# These can be used with Lists, Tuples and Dictionaries
li = [1,2,3,4]
def func(a,b,c,d):
    return a + b + c + d
print(func(*li))
# OUTPUT : 10
# Note : the number of elements in the list should be the same as the number of arguments
# Otherwise it will get error