# https://leetcode.com/problems/permutations-ii/

def permuteUniqueHelper(nums, ans, start):
    # base
    if start == len(nums):
        ans.append(nums[:])
        return

    visited = {}                                        #
    for i in range(start, len(nums)):
        if nums[i] in visited:                          # Another Approach
            continue                                    #

        visited[nums[i]] = True
        nums[i], nums[start] = nums[start], nums[i]
        permuteUniqueHelper(nums, ans, start + 1)
        nums[i], nums[start] = nums[start], nums[i]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        permuteUniqueHelper(nums, ans, 0)
        # st = set()
        # for e in ans:
        #     st.add(tuple(e))               
        # ans.clear()
        # for e in st:
        #     ans.append(list(e)) # only unique 
        return ans

        # per = permutations(nums)
        # l = []
        # for i in per:
        #     if i not in l:
        #         l.append(i)
        # return l      