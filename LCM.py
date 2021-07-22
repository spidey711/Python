#  Write a Python program to get the least common multiple (LCM) of two positive integers

def LCM(num1, num2):
    list1 = []
    list2 = []
    lcm_num = []
    for x in range(1, 11):
        list1.append(num1 * x)
    for y in range(1, 11):
        list2.append(num2 * y)
    for i in list1:
        for j in list2:
            if i == j:
                a = i = j
                lcm_num.append(a)
    print(min(lcm_num))


num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
res = LCM(num1, num2)
print(res)