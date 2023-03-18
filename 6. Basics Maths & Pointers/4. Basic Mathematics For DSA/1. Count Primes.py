# https://leetcode.com/problems/count-primes/description/

# CodeHelp

class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<=1):
            return 0

        sieve = [True] * n
        sieve[0] = sieve[1] = False

        for i in range(2,n):
            if sieve[i] == True:
                j = i*2
                while(j < n):
                    sieve[j] = False
                    j += i
        return sum(sieve)