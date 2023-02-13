n = int(input())


def DecimalToBinaryMethod2(n):
    # Bitwise Method
    binaryno = 0
    i = 0
    while n > 0:
        bit = (n & 1)
        i += 1
        binaryno = bit * (10 ** i) + binaryno
        n = n >> 1
    return binaryno

print(DecimalToBinaryMethod2(n))