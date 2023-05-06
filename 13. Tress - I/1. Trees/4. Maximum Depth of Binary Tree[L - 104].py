# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# CodeHelp

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        ans = max(left_height, right_height) + 1
        return ans