n = int(input())

for i in range(2*n-1):
    condition = 0

    if i < n: # growing phase of Diamond
        condition = i 

    else:     # shrinking phase of Diamond
        condition = n - (i % n) - 2

    for j in range(condition + 1):
        print("*",end='')
    print()
