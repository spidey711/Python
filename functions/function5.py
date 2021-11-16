# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

def func1(a, b):
    c = a + b
    def func2():
        return c + 5 
    return func2()

print(func1(1,3))