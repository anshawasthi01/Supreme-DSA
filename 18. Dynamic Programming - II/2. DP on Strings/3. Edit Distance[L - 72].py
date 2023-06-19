# https://leetcode.com/problems/edit-distance/

# Code Help

class Solution:
    def solveUsingRecursion(self, a, b, i, j):
        # Base case
        if i == len(a):
            return len(b) - j

        if j == len(b):
            return len(a) - i

        ans = 0
        if a[i] == b[j]:
            ans = self.solveUsingRecursion(a, b, i + 1, j + 1)
        else:
            # Perform operations
            insert = 1 + self.solveUsingRecursion(a, b, i, j + 1)
            delete = 1 + self.solveUsingRecursion(a, b, i + 1, j)
            replace = 1 + self.solveUsingRecursion(a, b, i + 1, j + 1)
            ans = min(insert, delete, replace)
        return ans

    def solveUsingMem(self, a, b, i, j, dp):
        # Base case
        if i == len(a):
            return len(b) - j

        if j == len(b):
            return len(a) - i

        if dp[i][j] != -1:
            return dp[i][j]

        ans = 0
        if a[i] == b[j]:
            ans = self.solveUsingMem(a, b, i + 1, j + 1, dp)
        else:
            # Perform operations
            insert = 1 + self.solveUsingMem(a, b, i, j + 1, dp)
            delete = 1 + self.solveUsingMem(a, b, i + 1, j, dp)
            replace = 1 + self.solveUsingMem(a, b, i + 1, j + 1, dp)
            ans = min(insert, delete, replace)
        dp[i][j] = ans
        return dp[i][j]

    def solveUsingTab(self, a, b):
        dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

        for j in range(len(b), -1, -1):
            dp[len(a)][j] = len(b) - j

        for i in range(len(a), -1, -1):
            dp[i][len(b)] = len(a) - i

        for i in range(len(a) - 1, -1, -1):
            for j in range(len(b) - 1, -1, -1):
                ans = 0
                if a[i] == b[j]:
                    ans = dp[i + 1][j + 1]
                else:
                    # Perform operations
                    insert = 1 + dp[i][j + 1]
                    delete = 1 + dp[i + 1][j]
                    replace = 1 + dp[i + 1][j + 1]
                    ans = min(insert, delete, replace)
                dp[i][j] = ans
        return dp[0][0]

    def solveUsingTabSO(self, a, b):
        # dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
        curr = [0] * (len(b) + 1)
        next = [0] * (len(b) + 1)

        for j in range(len(b) + 1):
            next[j] = len(b) - j

        for i in range(len(a) - 1, -1, -1):
            # every row starts here
            # yaha galti karoge
            curr[len(b)] = len(a) - i

            for j in range(len(b) - 1, -1, -1):
                ans = 0
                if a[i] == b[j]:
                    ans = next[j + 1]
                else:
                    # Perform operations
                    insert = 1 + curr[j + 1]
                    delete = 1 + next[j]
                    replace = 1 + next[j + 1]
                    ans = min(insert, delete, replace)
                curr[j] = ans
            next = curr.copy()
        return next[0]

    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)

        if len(word2) == 0:
            return len(word1)

        i = 0
        j = 0
        # return self.solveUsingRecursion(word1, word2, i, j)

        # dp = [[-1] * len(word2) for _ in range(len(word1))]
        # return self.solveUsingMem(word1, word2, i, j, dp)

        # return self.solveUsingTabSO(word1, word2)

        return self.solveUsingTabSO(word1, word2)





