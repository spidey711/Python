# display numbers between given range
li = []
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
for i in range(num1, num2):
    if i>1: # if i is 1 or 0, its neither composite nor real
        for j in range(2, i): # check for factors from 2 to a number
            if i%j==0: # if remainder = 0, then its composite
                break
        else:
            li.append(i) # if remainder not 0, append to list
print(f"Prime Numbers b/w {num1} and {num2} are: {','.join([str(i) for i in li])}")