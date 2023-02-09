num = int(input())

def allPrime(num):
    for num in range(2, num+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end= ', ')

allPrime(num)