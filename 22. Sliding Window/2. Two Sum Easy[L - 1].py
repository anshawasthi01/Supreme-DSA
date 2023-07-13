# https://leetcode.com/problems/two-sum/description/
# SLIDING WINDOWS
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = []
        ans = []

        for i in range(len(nums)):
            val = nums[i]
            index = i
            data.append((val, index))

        data.sort(key=lambda x: x[0])

        start = 0
        end = len(data) - 1

        while start < end:
            if data[start][0] + data[end][0] == target:
                ans.append(data[start][1])
                ans.append(data[end][1])
                break
            elif data[start][0] + data[end][0] > target:
                end -= 1
            else:
                start += 1

        return ans







#         for i, el1 in enumerate(nums):
#             for j, el2 in enumerate(nums):
#                 if el1+el2==target and i!=j:
#                     return [min(i,j),max(i,j)]
                
                
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         m={}
#         for i, el in enumerate(nums):
#              if target-el in m:
#                 return [m[target-el],i]
#              m[el]=i    

                