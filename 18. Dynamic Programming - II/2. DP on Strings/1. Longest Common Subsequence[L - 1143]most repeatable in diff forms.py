# https://leetcode.com/problems/longest-common-subsequence/

# CodeHelp
class Solution:
    def solveUsingRecursion(self, a, b, i, j):
        if i == len(a):
            return 0
        if j == len(b):
            return 0

        ans = 0
        if a[i] == b[j]:
            ans = 1 + self.solveUsingRecursion(a, b, i + 1, j + 1)
        else:
            ans = max(self.solveUsingRecursion(a, b, i, j + 1), self.solveUsingRecursion(a, b, i + 1, j))
        return ans

    def solveUsingMem(self, a, b, i, j, dp):
        if i == len(a):
            return 0
        if j == len(b):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        ans = 0
        if a[i] == b[j]:
            ans = 1 + self.solveUsingMem(a, b, i + 1, j + 1, dp)
        else:
            ans = max(self.solveUsingMem(a, b, i, j + 1, dp), self.solveUsingMem(a, b, i + 1, j, dp))
        dp[i][j] = ans
        return dp[i][j]

    def solveUsingTab(self, a, b):
        dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

        for i in range(len(a) - 1, -1, -1):
            for j in range(len(b) - 1, -1, -1):
                ans = 0
                if a[i] == b[j]:
                    ans = 1 + dp[i + 1][j + 1]
                else:
                    ans = max(dp[i][j + 1], dp[i + 1][j])
                dp[i][j] = ans

        return dp[0][0]

    def solveUsingTabSO(self, a, b):
        # dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
        curr = [0] * (len(b) + 1)
        next_ = [0] * (len(b) + 1)

        for i in range(len(a) - 1, -1, -1):
            for j in range(len(b) - 1, -1, -1):
                ans = 0
                if a[i] == b[j]:
                    ans = 1 + next_[j + 1]
                else:
                    ans = max(curr[j + 1], next_[j])
                curr[j] = ans

            # shift
            next_ = curr.copy()

        return next_[0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i = 0
        j = 0
        # return self.solveUsingRecursion(text1, text2, i, j)

        # dp = [[-1] * len(text2) for _ in range(len(text1))]
        # return self.solveUsingMem(text1, text2, i, j, dp)

        # return self.solveUsingTab(text1, text2)

        return self.solveUsingTabSO(text1, text2)



