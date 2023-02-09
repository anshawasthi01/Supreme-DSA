n = int(input())

def sumOfN(n):
    s = 0
    for i in range(2, n + 1, 2):
        s = s + i
    print(s)
    
sumOfN(n)
