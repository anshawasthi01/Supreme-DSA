def clearLastIBits(n, i):
    mask = (-1 << i)
    n = n & mask
    print("after clearing last", i, "bits:", n)
    
n = 7
clearLastIBits(n, 2)