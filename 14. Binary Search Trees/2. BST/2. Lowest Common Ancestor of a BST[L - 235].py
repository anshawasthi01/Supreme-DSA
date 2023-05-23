# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# CodeHelp

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # base case
        if not root:
            return None

        # case 1
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # case 2
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # case 3 and case 4
        else:
            return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
