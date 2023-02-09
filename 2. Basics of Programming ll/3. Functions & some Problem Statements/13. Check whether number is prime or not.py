n = int(input())

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

if prime(n):
    print(n, "Number is prime")
else:
    print(n, "Number is not prime")