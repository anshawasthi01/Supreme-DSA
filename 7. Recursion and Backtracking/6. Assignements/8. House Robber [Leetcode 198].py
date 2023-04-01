# https://leetcode.com/problems/house-robber/

# CodeHelp

def robHelper(nums, i):
    if i >= len(nums): return 0

    # Solution for 1 case
    robAmt1 = nums[i] + robHelper(nums, i+2)
    robAmt2 = 0 + robHelper(nums, i+1)

    return max(robAmt1, robAmt2)


class Solution:
    def rob(self, nums: List[int]) -> int:
        # # Iterative
        # for i in range(1, len(nums)):
        #     if i == 1:
        #         nums[i] = max(nums[i], nums[i-1])
        #     else:
        #         nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        # return nums[-1]

        return robHelper(nums, 0)
