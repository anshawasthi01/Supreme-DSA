# 7 https://leetcode.com/problems/reverse-integer/
# import sys  sys.maxsize-1  sys.maxsize 
  
# -2147483648 2147483647
class Solution:
    def reverse(self, x: int) -> int:
        ans, isNeg = 0, False

        if x <= -2147483648: #min_int
            return 0

        if x < 0:
            isNeg = True
            x = -x

        while x > 0:
            if ans > 2147483647/10:
                return 0

            digit = x % 10
            ans = ans * 10 + digit
            x = x // 10

        return -ans if isNeg else ans