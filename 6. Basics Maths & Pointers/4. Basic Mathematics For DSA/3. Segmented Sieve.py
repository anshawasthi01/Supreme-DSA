import math
def Sieve(n):
    if(n<=1):
        return 0

    sieve = [True] * n
    sieve[0] = sieve[1] = False

    for i in range(2,n):
        if i*i < n: # Optimization 2
            if sieve[i] == True:
                j = i*i # Optimization 1 : first unmarked number would be i*i,, as others have been marked by 2 to (i - 1)
                while(j < n):
                    sieve[j] = False
                    j += i
    return sieve

def segSieve(L, R):
    # get prime array, i will use it to mark segmented sieve

    sieve = Sieve(int(math.sqrt(R)))
    basePrimes = []

    for i in range(len(sieve)):
        if sieve[i]:
            basePrimes.append(i)

    segSieve = [True] * (R-L+1)
    if(L == 1 or L == 0):
        segSieve[L] = False

    for prime in basePrimes:
        first_mul = (L // prime) * prime
        if first_mul < L:
            first_mul += prime
        
        j = max(first_mul, prime * prime)
        while(j <= R):
            segSieve[j - L] = False
            j += prime
    return segSieve

L, R = 110, 130
ss = segSieve(L, R)
for i in range(len(ss)):
    if ss[i]:
        print(i + L, end = ' ')