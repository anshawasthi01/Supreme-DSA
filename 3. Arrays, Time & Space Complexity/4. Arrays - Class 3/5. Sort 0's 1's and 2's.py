# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        first, cur, last  = 0, 0, len(nums)-1
 
        while(cur<=last):
            if nums[cur] == 0:
                nums[first], nums[cur] = nums[cur], nums[first]
                cur+=1
                first+=1
            
            elif nums[cur] == 1:
                cur+=1
                
            else:
                nums[cur], nums[last] = nums[last], nums[cur]
                last-=1
        return nums