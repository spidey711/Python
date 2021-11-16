# Write a Python program to compute the greatest common divisor (GCD) of two positive integers

def GCD(num1, num2):
    list1 = []
    list2 = []
    gcd_num = []
    for x in range(1, num1+1):
        if num1 % x == 0:
            list1.append(x)
        else:
            pass
    for y in range(1, num2+1):
        if num2 % y == 0:
            list2.append(y)
        else:
            pass
    for i in list1:
        for j in list2:
            if i == j:
                a = i = j
                gcd_num.append(a)
            else:
                pass
    print(max(gcd_num))

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
res = GCD(num1, num2)
print(res)
