n = int(input())

for i in range(2*n):
    condition = i if i < n else n + (n - i - 1)
    space_count = 2 * (n - condition - 1) if i < n else i - condition - 1

    for j in range(2*n):
        if j <= condition:
            print("*",end='')

        elif space_count > 0:
            print(" ",end='')
            space_count -= 1

        else:
            print("*",end='')
    print()