res = 1
num1 = int(input("Enter number: "))
if num1 != 0:
    for i in range(1, num1+1):
        res *= i # res = res * i
    print(f'Factorial of {num1} is: {res}')
else:
    print(f'Factorial of {num1} is: 1')