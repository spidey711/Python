my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(my_list)):
    if i%2==0:
        continue
    else:
        print(my_list[i], end=' ')