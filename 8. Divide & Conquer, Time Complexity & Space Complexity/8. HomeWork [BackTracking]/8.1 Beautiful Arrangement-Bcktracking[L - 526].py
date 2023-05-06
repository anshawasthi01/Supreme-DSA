# https://leetcode.com/problems/beautiful-arrangement/description/

# CodeHelp

class Solution:
    def countArrangementHelper(self, v, n, ans, currNum):
        # Base case
        if currNum == n+1:
            # for i in range(n+1):
            #     print(v[i]," ")
            # print()
            ans += 1
            return ans
        for i in range(1, n+1):
            if v[i] == 0 and (currNum % i == 0 or i % currNum == 0):
                v[i] = currNum
                ans = self.countArrangementHelper(v, n, ans, currNum + 1)
                v[i] = 0  # Backtracking
        return ans

    def countArrangement(self, n: int) -> int:
        v = [0] * (n+1)
        ans = 0
        ans = self.countArrangementHelper(v, n, ans, 1)
        return ans
