# https://leetcode.com/problems/minimum-size-subarray-sum/
# CodeHelp

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        _sum = 0
        _len = float('inf')

        while j < len(nums):
            # Include the current number
            _sum += nums[j]
            # mere paas ek window ka sum ready h 
            # Check if the sum meets the target
            while _sum >= target:
                # minimise -> sum me se decrease karo, len bhi update krelna, i/start ko aage badhana padega
                _len = min(_len, j - i + 1)
                _sum -= nums[i]
                i += 1

            j += 1

        if _len == float('inf'):
            return 0
        else:
            return _len


        # n=len(nums)
        # i=j=0
        # s=nums[0]
        # m=9999999
        # while j<n and i<=j:
        #     if s>=target:   
        #         m=min(m,j-i+1)
        #         s-=nums[i]
        #         i+=1
        #     else:
        #         j+=1
        #         if j<n:
        #             s+=nums[j]
        # if m!=9999999:
        #     return m
        # return 0