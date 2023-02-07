n = int(input())

for r in range(n):
    for c in range(r): #space
        print(" ",end='')

    for c in range(n - r): #stars
        print("* ",end='')
    
    print()
