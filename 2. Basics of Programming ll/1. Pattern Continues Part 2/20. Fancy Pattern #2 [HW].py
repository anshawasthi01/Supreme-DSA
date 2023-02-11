# N = 4
n = int(input())
c = 1
for i in range(n):
    for j in range(i+1):
        print(c,end='')
        c += 1
        if j < i:
            print("*",end='')
    print()

# shrinking phase
start = c - n 
for i in range(n):
    k = start
    for j in range(n - i):
        print(k,end='')
        k += 1
        if j < n - i - 1:
            print("*",end='')
    
    start = start - (n - i - 1)
    print()
