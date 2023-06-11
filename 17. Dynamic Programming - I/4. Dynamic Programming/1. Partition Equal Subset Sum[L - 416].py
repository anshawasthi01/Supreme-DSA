# https://leetcode.com/problems/partition-equal-subset-sum/description/

# CodeHelp

class Solution:
    def solveUsingRecursion(self, index, nums, target):
        # base case
        n = len(nums)
        if index >= n:
            return False

        if target < 0:
            return False

        if target == 0:
            return True

        include = self.solveUsingRecursion(index + 1, nums, target - nums[index])
        exclude = self.solveUsingRecursion(index + 1, nums, target)

        return include or exclude

    def solveUsingMem(self, index, nums, target, dp):
        # base case
        n = len(nums)
        if index >= n:
            return False

        if target < 0:
            return False

        if target == 0:
            return True

        if dp[index][target] != -1:
            return dp[index][target]

        include = self.solveUsingMem(index + 1, nums, target - nums[index], dp)
        exclude = self.solveUsingMem(index + 1, nums, target, dp)

        dp[index][target] = include or exclude
        return dp[index][target]

    def solveUsingTabulation(self, nums, target, dp):
        n = len(nums)

        for i in range(n):
            dp[i][0] = True

        for index in range(n - 1, -1, -1):
            for t in range(1, target + 1):
                include = False

                if t - nums[index] >= 0:
                    include = dp[index + 1][t - nums[index]]
                exclude = dp[index + 1][t]

                dp[index][t] = include or exclude
        return dp[0][target]

    def solveUsingTabulationSO(self, nums, target):
        n = len(nums)

        curr = [0] * (target + 1)
        nxt = [0] * (target + 1)

        curr[0] = 1
        nxt[0] = 1

        for index in range(n - 1, -1, -1):
            for t in range(1, target + 1):
                include = False
                if t - nums[index] >= 0:
                    include = nxt[t - nums[index]]

                exclude = nxt[t]

                curr[t] = include or exclude
            nxt = curr[:]
        return nxt[target]

    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)

        # yha hi galti karunga
        if summ & 1:
            return False

        target = summ // 2

        # index = 0
        # ans = self.solveUsingRecursion(index, nums, target)

        # dp = [[-1] * (target + 1) for _ in range(len(nums))]
        # ans = self.solveUsingMem(index, nums, target, dp)

        # n = len(nums)
        # dp = [[0] * (target + 1) for _ in range(n + 1)]
        # ans = self.solveUsingTabulation(nums, target, dp)

        ans = self.solveUsingTabulationSO(nums, target)

        # for i in range(n + 1):
        #     for j in range(target + 1):
        #         print(dp[i][j], end=' ')
        #     print()

        return ans
