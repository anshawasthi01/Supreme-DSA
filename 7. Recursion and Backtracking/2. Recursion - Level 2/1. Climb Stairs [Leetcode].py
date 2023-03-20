# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)






        # if n <= 2:
        #     return n
        
        # prev1 = 1
        # prev2 = 1
        # current = 0
        # for i in range(2, n+1):
        #     current = prev1 + prev2
        #     prev1 = prev2
        #     prev2 = current
            
        # return current
        




        