# https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/

# CodeHelp

class Solution:
    def solveUsingRecursion(self, start, end):
        if start >= end:
            return 0
        
        ans = float('inf')
        for i in range(start, end + 1):
            ans = min(ans, i + max(self.solveUsingRecursion(start, i - 1), self.solveUsingRecursion(i + 1, end)))
        
        return ans

    def solveUsingMem(self, start, end, dp):
        if start >= end:
            return 0

        if dp[start][end] != -1:
            return dp[start][end]

        ans = float('inf')
        for i in range(start, end + 1):
            ans = min(ans, i + max(self.solveUsingMem(start, i - 1, dp), self.solveUsingMem(i + 1, end, dp)))
        
        dp[start][end] = ans
        return dp[start][end]

    def solveUsingTab(self, n):
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for start in range(n, 0, -1):
            for end in range(1, n + 1):
                if start >= end:
                    continue
                else:
                    ans = float('inf')
                    for i in range(start, end + 1):
                        ans = min(ans, i + max(dp[start][i - 1], dp[i + 1][end]))
                    
                    dp[start][end] = ans
        
        return dp[1][n]

    def getMoneyAmount(self, n: int) -> int:
        # ans = self.solveUsingRecursion(1, n)

        # dp = [[-1] * (n + 1) for _ in range(n + 1)]
        # ans = self.solveUsingMem(1, n, dp)

        ans = self.solveUsingTab(n)
        return ans
