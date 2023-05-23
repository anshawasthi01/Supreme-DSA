# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

# CodeHelp

class Solution:
    def store_inorder(self, root, inorder):
        if root is None:
            return
        self.store_inorder(root.left, inorder)
        inorder.append(root.val)
        self.store_inorder(root.right, inorder)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder = []
        self.store_inorder(root, inorder)

        start = 0
        end = len(inorder) - 1

        while start < end:
            total = inorder[start] + inorder[end]

            if total == k:
                return True

            if total > k:
                end -= 1
            else:
                start += 1

        return False

