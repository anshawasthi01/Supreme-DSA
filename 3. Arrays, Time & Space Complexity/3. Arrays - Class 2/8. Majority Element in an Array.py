# https://leetcode.com/problems/majority-element/

# Moore's Voting Algo (Most Imp)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == curr:
                count += 1
            else:
                count -= 1
                
                if count == 0:
                    count = 1
                    curr = nums[i]
        return curr


                
        
        
        
        
      
