# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = ""
        for c in s:
            if len(ans) < 1:
                ans += c
            elif c == ans[-1]:
                ans = ans[:-1]
            else:
                ans += c
        return ans