# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# CodeHelp
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if root is None:
            return None

        # check for p and q
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q

        leftAns = self.lowestCommonAncestor(root.left, p, q)
        rightAns = self.lowestCommonAncestor(root.right, p, q)

        if leftAns is None and rightAns is None:
            return None
        elif leftAns is not None and rightAns is None:
            return leftAns
        elif leftAns is None and rightAns is not None:
            return rightAns
        else:
            return root
