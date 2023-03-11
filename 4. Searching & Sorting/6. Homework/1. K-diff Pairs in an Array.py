# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# CodeHelp

def bs(nums, start, x):
    end = len(nums)-1
    while start <= end:
        mid = (start + end )//2
        if nums[mid] == x:
            return mid
        elif x > nums[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            if bs(nums, i+1, nums[i]+k) != -1:
                ans.add((nums[i], nums[i]+k))
        return len(ans)

