n = int(input())

for r in range(n):
    for c in range(n - r - 1): #spaces
        print(" ",end='')

    for c in range(2 * r + 1): #stars
        if c == 0 or c == 2 * r:  #if first character or if last character
            print("*",end='') # first character or last character

        else:
            print(" ",end='')
    print()

for r in range(n):
    for c in range(r): #spaces
        print(" ",end='')

    for c in range(2 * n - 2 * r - 1): #star
        if c == 0 or c == 2 * n - 2 * r - 2: #if first or last character
            print("*",end='')
        else:
            print(" ",end='')
    print()

