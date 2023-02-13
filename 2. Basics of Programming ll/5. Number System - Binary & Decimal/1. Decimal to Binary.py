n = int(input())

def DecimalToBinaryMethod1(n):
    # Division method
    while n > 0:
        bit = n % 2
        print(bit)
        n = n // 2

DecimalToBinaryMethod1(n)