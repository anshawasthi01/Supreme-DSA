n = int(input())

def BinaryToDecimal(n):
    decimal = 0
    i = 0
    while n:
        bit = n % 10
        i += 1
        decimal = decimal + bit * (2 ** i)
        n //= 10
    return decimal

print(BinaryToDecimal(n))