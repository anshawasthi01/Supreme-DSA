# https://leetcode.com/problems/longest-increasing-subsequence/description/

# CodeHelp

class Solution:
    def solveUsingRecursion(self, arr, curr, prev):
        if curr >= len(arr):
            return 0

        # include
        include = 0
        if prev == -1 or arr[curr] > arr[prev]:
            include = 1 + self.solveUsingRecursion(arr, curr+1, curr)

        # exclude
        exclude = 0 + self.solveUsingRecursion(arr, curr+1, prev)

        ans = max(include, exclude)
        return ans

    def solveUsingMem(self, arr, curr, prev, dp):
        if curr >= len(arr):
            return 0

        if dp[curr][prev + 1] != -1:
            return dp[curr][prev+1]

        # include
        include = 0
        if prev == -1 or arr[curr] > arr[prev]:
            include = 1 + self.solveUsingMem(arr, curr+1, curr, dp)

        # exclude
        exclude = 0 + self.solveUsingMem(arr, curr+1, prev, dp)

        dp[curr][prev + 1] = max(include, exclude)
        return dp[curr][prev + 1]

    def solveUsingTab(self, arr):
        n = len(arr)
        dp = [[0] * (n+1) for _ in range(n+1)]

        for curr in range(n-1, -1, -1):
            for prev in range(curr - 1, -2, -1):
                # include
                include = 0
                if prev == -1 or arr[curr] > arr[prev]:
                    include = 1 + dp[curr+1][curr + 1]

                # exclude
                exclude = 0 + dp[curr+1][prev + 1]

                dp[curr][prev + 1] = max(include, exclude)
        return dp[0][0]

    def solveOptimal(self, arr):
        if len(arr) == 0:
            return 0
        ans = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i] > ans[-1]:
                # include
                ans.append(arr[i])
            else:
                # overwrite
                # find index of the first greater element
                # find index of just bada element
                index = self.lower_bound(ans, arr[i])
                ans[index] = arr[i]
        return len(ans)

    def lower_bound(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def lengthOfLIS(self, nums: List[int]) -> int:
        curr = 0
        prev = -1
        # ans = self.solveUsingRecursion(nums, curr, prev)

        # n = len(nums)
        # dp = [[-1] * (n+1) for _ in range(n)]
        # ans = self.solveUsingMem(nums, curr, prev, dp)

        # ans = self.solveUsingTab(nums)

        ans = self.solveOptimal(nums)
        return ans
