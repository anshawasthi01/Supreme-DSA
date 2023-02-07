n = int(input())

for r in range(n):
    for c in range(n - r): #half pyrmaid
        print("*",end='')
    
    for c in range(2 * r + 1): #space wlaa full puramid
            print(" ",end = '') 

    for c in range(n - r): #half pyramid
        print("*",end='')
    print()

for r in range(n):
    for c in range(r + 1): #half pyrmaid
        print("*",end='')

    for c in range(2 * n - 2 * r - 1): #space wlaa full puramid
            print(" ",end = '') 

    for c in range(r + 1): #half pyramid
        print("*",end='')
    print()


