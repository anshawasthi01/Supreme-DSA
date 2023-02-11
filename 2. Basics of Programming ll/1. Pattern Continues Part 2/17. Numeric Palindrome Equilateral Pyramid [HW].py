n = int(input())

k = n
for i in range(n):
    c = 1
    for j in range(k):
        if (j < n - i - 1):
            print(" ",end='')
        elif j <= n-1:
            print(c,end='')
            c += 1

        elif j == n:
            c = c - 2
            print(c,end='')
            c -= 1

        else:
            print(c,end='')
            c -= 1
    k +=1 

    print()