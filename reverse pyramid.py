# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
n, k = 5, 5
for i in range(0, n+1):          # 0 1 2 3 4 5
    for j in range(k-i, 0, -1):  # 5 4 3 2 1 0, first iteration=54321, second iteration=4321 so on and so forth
        print(j, end=' ')
    print()
        