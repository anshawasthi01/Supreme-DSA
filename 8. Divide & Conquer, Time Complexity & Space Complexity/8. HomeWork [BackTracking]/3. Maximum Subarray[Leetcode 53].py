# CodeHelp Recursion
def SubArray(a, s, e):
    if s == e: return a[s]
    maxLeftBorderSum, maxRightBorderSum = -99999999, -9999999
    mid = s + ((e - s) >> 1)

    maxLeftSum = SubArray(a, s, mid)
    maxRightSum = SubArray(a, mid + 1, e)

    # Max Cross Border Sum
    leftBorderSum, rightBorderSum = 0, 0

    for i in range(mid, s-1, -1):
        leftBorderSum += a[i]
        if leftBorderSum > maxLeftBorderSum: maxLeftBorderSum = leftBorderSum

    for i in range(mid + 1, e + 1):
        rightBorderSum += a[i]
        if rightBorderSum > maxRightBorderSum: maxRightBorderSum = rightBorderSum

    crossBorderSum = maxLeftBorderSum + maxRightBorderSum
    return max(maxLeftSum, maxRightSum, crossBorderSum)

class Solution(object):
    def maxSubArray(self, nums):
        return SubArray(nums, 0, len(nums) - 1)
        


        '''
        n = len(nums)
        max_sum = nums[0]
        prev_sum = 0
        curr_sum = -1
        for i in range(n):
            curr_sum = prev_sum + nums[i]
            max_sum = max(curr_sum,max_sum)
            prev_sum = max(curr_sum,0)
        return max_sum
        
        
        # kadane's algo # Devsnest
        maxSum = -999999
        curSum = 0
        for num in nums:
            curSum+=num 
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
        return maxSum
        '''
        