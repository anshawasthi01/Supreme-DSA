# https://leetcode.com/problems/house-robber/

# CodeHelp

class Solution:
    # n -> represents the index of current house
    def solveUsingRecursion(self, nums, n):
        if n < 0:
            return 0
        if n == 0:
            return nums[0]

        # include
        include = self.solveUsingRecursion(nums, n - 2) + nums[n]
        exclude = self.solveUsingRecursion(nums, n - 1) + 0

        return max(include, exclude)


    def solveUsingMem(self, nums, n, dp):
        if n < 0:
            return 0
        if n == 0:
            return nums[0]

        if dp[n] != -1:
            return dp[n]

        # include
        include = self.solveUsingMem(nums, n - 2, dp) + nums[n]
        exclude = self.solveUsingMem(nums, n - 1, dp) + 0

        dp[n] = max(include, exclude)
        return dp[n]


    def solveUsingTabulation(self, nums, n):
        dp = [0] * (n + 1)
        dp[0] = nums[0]

        for i in range(1, n + 1):
            temp = 0
            if i - 2 >= 0:
                temp = dp[i - 2]

            include = temp + nums[i]
            exclude = dp[i - 1] + 0

            dp[i] = max(include, exclude)

        return dp[n]


    def spaceOptimisedSolution(self, nums, n):
        prev2 = 0
        prev1 = nums[0]
        # dp = [0] * (n + 1)
        # dp[0] = nums[0]
        curr = 0

        for i in range(1, n + 1):
            temp = 0
            if i - 2 >= 0:
                temp = prev2

            include = temp + nums[i]
            exclude = prev1 + 0

            curr = max(include, exclude)
            prev2 = prev1
            prev1 = curr

        return prev1


    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        # return self.solveUsingRecursion(nums, n)

        # dp = [-1] * (n + 1)
        # return self.solveUsingMem(nums, n, dp)

        # return self.solveUsingTabulation(nums, n)

        return self.spaceOptimisedSolution(nums, n)




























# RECURSION Lakshay
# def robHelper(nums, i):
#     if i >= len(nums): return 0

#     # Solution for 1 case
#     robAmt1 = nums[i] + robHelper(nums, i+2)
#     robAmt2 = 0 + robHelper(nums, i+1)

#     return max(robAmt1, robAmt2)


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # # Iterative
#         # for i in range(1, len(nums)):
#         #     if i == 1:
#         #         nums[i] = max(nums[i], nums[i-1])
#         #     else:
#         #         nums[i] = max(nums[i] + nums[i-2], nums[i-1])
#         # return nums[-1]

#         return robHelper(nums, 0)

