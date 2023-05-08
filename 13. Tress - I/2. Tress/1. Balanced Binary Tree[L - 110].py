# CodeHelp
# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: TreeNode) -> int:
        # base case
        if not root:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        ans = 1 + max(left_height, right_height)
        return ans
    
    def isBalanced(self, root: TreeNode) -> bool:
        # base case
        if not root:
            return True

        # case 1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        diff = abs(left_height - right_height)

        ans1 = (diff <= 1)

        # recursion
        left_ans = self.isBalanced(root.left)
        right_ans = self.isBalanced(root.right)

        if ans1 and left_ans and right_ans:
            return True
        else:
            return False
