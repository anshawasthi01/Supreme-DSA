def findMissing(a, n):
    # visited method
    for i in range(n):
        index = abs(a[i])
        if a[index-1] > 0:
            a[index-1] *= -1

    for i in range(n):
        if a[i] > 0:
            print(i+1)

def findMissing1(a, n):
    # sorting + swapping method
    i = 0
    while i < n:
        index = a[i] - 1
        if a[i] != a[index]:
            a[i], a[index] = a[index], a[i]
        else:
            i += 1

    for i in range(n):
        if a[i] != i+1:
            print(i+1)

a = [1, 3, 3, 3, 6, 6]
n = len(a)
# findMissing(a, n)
findMissing1(a, n)
