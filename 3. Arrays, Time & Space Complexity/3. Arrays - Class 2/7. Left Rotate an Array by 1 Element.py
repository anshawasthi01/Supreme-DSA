# https://leetcode.com/problems/rotate-array/
# CodeHelp

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        temp = nums[:]

        for i in range(n):
            temp[(i + k) % n]  = nums[i]
        
        nums[:] = temp


		