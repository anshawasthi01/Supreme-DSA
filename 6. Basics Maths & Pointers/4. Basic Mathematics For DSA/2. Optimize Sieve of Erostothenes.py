# https://leetcode.com/problems/count-primes/description/

# CodeHelp

class Solution:
    def countPrimes(self, n: int) -> int:
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
        return sum(sieve)

#         if(n<=1):
#             return 0
#         d  = [True] * n
#         d[0] = d[1] = False
#         for i in range(2,n):
#             if(d[i]):
#                 for j in range(i*i,n,i):
#                     d[j] = False
#         return sum(d)