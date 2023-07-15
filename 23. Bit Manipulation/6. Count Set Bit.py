def countSetBits(n):
    count = 0
    while n != 0:
        last_bit = n & 1
        if last_bit:
            count += 1
        # right shift
        n = n >> 1
    return count

def countSetBitsFast(n):
    count = 0
    while n != 0:
        # remove last set bit
        n = n & (n - 1)
        count += 1
    return count
    
print("Number of set bits:", countSetBits(1024))
print("Number of set bits:", countSetBitsFast(1024))