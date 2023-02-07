n = int(input())

for r in range(n):
    for c in range(n - r - 1): #space
        print(" ",end='')

    for c in range(r + 1): #stars
        print("* ",end='')
    
    print()

    
