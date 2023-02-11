n = int(input())

for i in range(n):
    condition = 2*i if (i <= n/2) else (2 * (n-i-1))
    for j in range(condition+1):
        if j <= condition/2:
            print(j+1,end='')
        else:
            print(condition-j+1,end='')
    print()