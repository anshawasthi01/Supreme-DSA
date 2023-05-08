# https://leetcode.com/problems/path-sum-ii/

# CodeHelp

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def solve(root, targetSum, currSum, path, ans):
            # print("Curr Sum ", currSum )
            # base case
            if not root:
                return
            
            # leaf node
            if not root.left and not root.right:
                # include current node
                path.append(root.val)
                currSum += root.val
                # check for target sum
                if currSum == targetSum:
                    ans.append(path[:])
                # exclude current node
                path.pop()
                currSum -= root.val
                return
            
            # include current node
            path.append(root.val)
            currSum += root.val
            
            solve(root.left, targetSum, currSum, path, ans)
            solve(root.right, targetSum, currSum, path, ans)
            
            # backtrack
            path.pop()
            currSum -= root.val
        
        ans = []
        path = []
        currSum = 0
        solve(root, targetSum, currSum, path, ans)
        return ans
