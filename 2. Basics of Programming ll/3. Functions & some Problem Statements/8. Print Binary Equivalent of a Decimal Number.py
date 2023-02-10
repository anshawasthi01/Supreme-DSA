# Taking binary input
binary = input("Enter a binary number:")



def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print("The decimal value is:", decimal)

# Calling the function
BinaryToDecimal(binary)


decimal = input("Enter a decimal number :")

def DecimalToBinary(decimal):
    if decimal > 1:
        DecimalToBinary(decimal // 2)
    print(decimal % 2, end = '')

# Calling the function
DecimalToBinary(int(decimal))





















# def binaryToDecimal(b):
#     ans=0
#     c=0
#     while b:
#         ans =  ans + b%10 * (1 << c++)
#         b/=10
#     return ans

