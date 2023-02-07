row = int(input())

for r in range(row):
    for c in range(row-r):
        print("*",end='')
    print()