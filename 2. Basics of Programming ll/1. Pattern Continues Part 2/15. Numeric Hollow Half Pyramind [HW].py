n = int(input())

for i in range(n):
    for j in range(i+1):
        if (j == 0 ) or (j == i) or (i == n-1):
            print(j+1,end='')
        else:
            print(" ",end='')

    print()