num = int(input())

def printNum(num):
    while num > 0:
        print(num % 10)
        num = int(num / 10)

printNum(num)

# while num != 0:
#     rem = num % 10
#     print(rem)
#     num = num / 10

# for n in range(num, 0, num = num/10):
#     rem = n % 10
#     print(rem)
