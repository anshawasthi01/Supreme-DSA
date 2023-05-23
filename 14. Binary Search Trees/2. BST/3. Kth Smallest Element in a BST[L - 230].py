# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# CodeHelp

class Solution:
    def kSmallest(self, root, c):
        # Base case
        if root is None:
            # -1 reflects base condition reached
            return -1

        # Inorder traversal

        # Left
        leftAns = self.kSmallest(root.left, c)

        if leftAns != -1:
            return leftAns

        # N.root
        c[0] -= 1
        if c[0] == 0:
            return root.val

        # Right
        rightAns = self.kSmallest(root.right, c)
        return rightAns

    def kthSmallest(self, root, k):
        c = [k]
        return self.kSmallest(root, c)
