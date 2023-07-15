def clearBitsInRange(n, i, j):
    # mask
    a = (-1 << (i + 1))
    b = (1 << j) - 1
    mask = a | b
    n = n & mask
    print("after clearing in range:", n)

clearBitsInRange(15, 3, 0)