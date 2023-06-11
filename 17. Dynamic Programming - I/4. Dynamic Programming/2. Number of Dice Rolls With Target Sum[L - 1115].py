# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/

# CodeHelp

class Solution:
    MOD = 10**9 + 7

    def solveUsingRecursion(self, n, k, target):
        # base case
        if n < 0:
            return 0
        if n == 0 and target == 0:
            return 1
        if n == 0 and target != 0:
            return 0
        if n != 0 and target == 0:
            return 0

        ans = 0
        for i in range(1, k+1):
            ans += self.solveUsingRecursion(n-1, k, target-i)
        return ans

    def solveUsingMem(self, n, k, target, dp):
        if n < 0:
            return 0
        if n == 0 and target == 0:
            return 1
        if n == 0 and target != 0:
            return 0
        if n != 0 and target == 0:
            return 0

        if dp[n][target] != -1:
            return dp[n][target]

        ans = 0
        for i in range(1, k+1):
            recAns = 0
            if target - i >= 0:
                recAns = self.solveUsingMem(n-1, k, target-i, dp)
            ans = (ans + recAns) % self.MOD

        dp[n][target] = ans
        return dp[n][target]

    def solveUsingTabulation(self, n, k, target):
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for index in range(1, n + 1):
            for t in range(1, target + 1):
                ans = 0
                for i in range(1, k + 1):
                    if t - i >= 0:
                        ans = (ans + dp[index-1][t-i]) % self.MOD
                dp[index][t] = ans

        return dp[n][target]

    def solveUsingTabulationSO(self, n, k, target):
        prev = [0] * (target + 1)
        curr = [0] * (target + 1)
        prev[0] = 1

        for index in range(1, n + 1):
            for t in range(1, target + 1):
                ans = 0
                for i in range(1, k + 1):
                    if t - i >= 0:
                        ans = (ans + prev[t-i]) % self.MOD
                curr[t] = ans
                # shift
            prev = curr[:]
        
        return prev[target]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # return self.solveUsingRecursion(n, k, target)

        # dp = [[-1] * (target + 1) for _ in range(n + 1)]
        # return self.solveUsingMem(n, k, target, dp)

        # return self.solveUsingTabulation(n, k, target)

        return self.solveUsingTabulationSO(n, k, target)


























# RECURSION TLE
# class Solution:
#     def numRollsToTarget(self, n: int, k: int, target: int) -> int:
#         # base
#         if target < 0: return 0
#         if n == 0 and target == 0: return 1
#         if n == 0 and target != 0: return 0
#         if n != 0 and target == 0: return 0

#         ans = 0
#         for i in range(1, k+1):
#             ans = ans + self.numRollsToTarget(n - 1, k, target - i)
#         return ans