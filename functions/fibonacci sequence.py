# upto 10 terms
def fibonacci():
    num1 = 0 
    num2 = 1
    for i in range(10):
        # add values
        res = num1 + num2
        print(num1, end=' ')
        # update values
        num1, num2 = num2, res
fibonacci()