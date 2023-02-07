# Printing Solid rectangle

row, col = map(int, input().split())

for r in range(row): # outer loop - row obeserve
    for c in range(col):  # inner loop - col observe
        print("*", end=' ') 
    print()