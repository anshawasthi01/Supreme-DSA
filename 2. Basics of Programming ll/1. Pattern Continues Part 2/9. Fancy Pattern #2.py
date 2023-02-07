n = int(input())

for r in range(n):
    for c in range(r + 1):
        print(r + 1, end='')
        if c != r:
            print("*",end='')
    print()

for r in range(n):
    for c in range(n - r):
        print(n - r, end='')
        if c != n - r - 1:
            print("*",end='')
    print()


