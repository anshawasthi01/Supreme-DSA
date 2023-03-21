# https://leetcode.com/problems/add-strings/
# LeetCode : 415

def addRE(num1, p1, num2, p2, carry, ans):
    # base case
    if p1 < 0 and p2 < 0:
        if carry != 0:
            ans.append(chr(carry))
        return

    # ek case solve
    n1 = num1[p1] if p1 >= 0 else '0'
    n2 = num2[p2] if p2 >= 0 else '0'
    csum = int(n1) + int(n2) + carry
    digit = csum % 10
    ans.append(chr(digit))

    # RE
    addRE(num1, p1 - 1, num2, p2 - 1, carry, ans)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        addRE(num1, len(num1) - 1, num2, len(num2) - 1, 0, ans)
        ans.reverse()
        return "".join(ans)


