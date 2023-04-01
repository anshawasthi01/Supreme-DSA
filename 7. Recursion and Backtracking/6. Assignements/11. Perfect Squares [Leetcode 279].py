# https://leetcode.com/problems/perfect-squares/description/

import math

def Helper(n):
    # base
    if n == 0: return 1
    if n < 0: return 0

    ans = 100000
    i = 1
    end = math.sqrt(n)
    while i <= end:
        perfectSquare = i * i
        numberOfPerfectSquares = 1 + Helper(n - perfectSquare)
        if numberOfPerfectSquares < ans:
            ans = numberOfPerfectSquares
        i += 1

    return ans

class Solution:
    def numSquares(self, n: int) -> int:
        return Helper(n) - 1
