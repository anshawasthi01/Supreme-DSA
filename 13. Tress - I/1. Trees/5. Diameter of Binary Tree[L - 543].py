# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        ans = max(leftHeight, rightHeight) + 1
        return ans
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        op1 = self.diameterOfBinaryTree(root.left)
        op2 = self.diameterOfBinaryTree(root.right)
        op3 = self.maxDepth(root.left) + self.maxDepth(root.right)
        ans = max(op1, op2, op3)
        return ans





















    #     def height(root):
    #         nonlocal diameter
    #         if not root:
    #             return 0
            
    #         left = height(root.left)
    #         right = height(root.right)
    #         diameter = max(diameter, left + right)
    #         return max(left, right) + 1
        
    #     diameter = 0
    #     height(root)
    #     return diameter