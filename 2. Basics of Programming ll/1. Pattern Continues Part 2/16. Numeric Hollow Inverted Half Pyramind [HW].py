n = int(input())

for i in range(n):
    for j in range(i+1,n+1):
        if (j == i+1 ) or (j == n) or (i == 0):
            print(j,end='')
        else:
            print(" ",end='')

    print()