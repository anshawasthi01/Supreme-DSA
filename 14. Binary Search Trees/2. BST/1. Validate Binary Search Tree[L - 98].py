# https://leetcode.com/problems/validate-binary-search-tree/description/

# CodeHelp
class Solution:
    def solve(self, root, lb, ub):
        if not root:
            return True

        if lb < root.val < ub:
            left_ans = self.solve(root.left, lb, root.val)
            right_ans = self.solve(root.right, root.val, ub)
            return left_ans and right_ans
        else:
            return False

    def isValidBST(self, root):
        lower_bound = float('-inf')
        upper_bound = float('inf')
        ans = self.solve(root, lower_bound, upper_bound)
        return ans
