# 2 22 222 2222 22222 = ?
num = 2
num_terms = 5
sum_seq = 0
for i in range(1, num_terms+1): # 1,2,3,4,5
    print(num, end=' ') # 2 2 2 2 2
    sum_seq += num      # 222 (2+22+222+...+22222)
    num = num*10+2      # 220+2=222
print(f'\nSum sequence: {sum_seq}')