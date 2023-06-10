# https://leetcode.com/problems/fibonacci-number/description/

# CodeHelp

class Solution:
    def recSolve(self, n):
        # base case
        if n == 0 or n == 1:
            return n
        ans = self.recSolve(n-1) + self.recSolve(n-2)
        return ans

    # Recursion + Memoisation
    def topDownSolve(self, n, dp):
        # base case
        if n == 1 or n == 0:
            return n
        
        # step3: check if aNS ALREADY EXIst
        if dp[n] != -1:
            return dp[n]

        # step2: replace ans woth dp[n]
        dp[n] = self.topDownSolve(n-1, dp) + self.topDownSolve(n-2, dp)
        return dp[n]

    # tabulation method
    def bottomUpSolve(self, n):
        # step1: create a dp array
        dp = [-1] * (n+1)
        # step2:base case
        dp[0] = 0
        if n == 0:
            return dp[0]
        dp[1] = 1
        # step3: topDown approach me n kaise travel krra
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def spaceOptSolve(self, n):
        # step2:base case
        prev2 = 0
        prev1 = 1
        if n == 0:
            return prev2
        if n == 1:
            return prev1
        curr = 0
        # step3: topDown approach me n kaise travel krra h 
        for i in range(2, n+1):
            curr = prev1 + prev2
            # shifting
            prev2, prev1 = prev1, curr
        return curr

    def fib(self, n: int) -> int:
        # step1: create dp array
        # dp = [-1] * (n + 1)
        # ans = self.topDownSolve(n, dp)
        # return ans
        return self.recSolve(n)
