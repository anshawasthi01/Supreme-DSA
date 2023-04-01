# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

# CodeHelp
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # base
        if target < 0: return 0
        if n == 0 and target == 0: return 1
        if n == 0 and target != 0: return 0
        if n != 0 and target == 0: return 0

        ans = 0
        for i in range(1, k+1):
            ans = ans + self.numRollsToTarget(n - 1, k, target - i)
        return ans