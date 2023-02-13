n = int(input())

# def DecimalToBinaryMethod1(n):
#     # Division method
#     while n > 0:
#         bit = n % 2
#         print(bit)
#         n = n // 2

def DecimalToBinaryMethod1(n):
    # Division method
    binaryno = 0
    i = 0
    while n > 0:
        bit = n % 2
        i += 1
        binaryno = bit * (10 ** i) + binaryno
        n = n // 2
    return binaryno

print(DecimalToBinaryMethod1(n))