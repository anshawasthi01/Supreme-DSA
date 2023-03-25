# https://leetcode.com/problems/generate-parentheses/description/


# CodeHelp

class Solution:
    def solve(self, ans: List[str], n: int, used_open: int, used_close: int, rem_open: int, rem_close: int, output: str) -> None:
        # base case
        if rem_open == 0 and rem_close == 0:
            ans.append(output)
            return

        # include open bracket
        if rem_open > 0:
            # output += '('
            self.solve(ans, n, used_open+1, used_close, rem_open-1, rem_close, output + '(')
            # backtrack
            # output = output[:-1]

        # include close bracket
        if used_open > used_close:
            # output += ')'
            self.solve(ans, n, used_open, used_close+1, rem_open, rem_close-1, output + ')')
            # backtrack
            # output = output[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        used_open = 0
        used_close = 0
        rem_open = n
        rem_close = n
        output = ""
        self.solve(ans, n, used_open, used_close, rem_open, rem_close, output)
        return ans

