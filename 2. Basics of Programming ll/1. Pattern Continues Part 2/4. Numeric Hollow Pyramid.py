# HW
n = int(input())

for r in range(n):
    for c in range(n - r - 1): #spaces
        print(" ",end='')

    start = 1
    for c in range(2 * r + 1):
        if r == 0 or r == n-1: #first row or last row 
            if c % 2 == 0: #even
                print(start,end='')
                start = start + 1
            else:
                print(" ",end='') #odd
        else:
            if c == 0:
                print(1,end='') # first col
            elif c == 2 * r + 1 - 1:
                print(r + 1,end='')
            else:
                print(" ",end='')
    print()