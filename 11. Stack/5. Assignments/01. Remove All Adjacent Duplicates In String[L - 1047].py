# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/


# CodeHelp Stack
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []

        for c in s:
            if st and st[-1] == c:
                st.pop()
            else:
                st.append(c)

        ans = ""
        while st:
            ans += st.pop()

        return ans[::-1]












































        # ans = ""
        # for c in s:
        #     if len(ans) < 1:
        #         ans += c
        #     elif c == ans[-1]:
        #         ans = ans[:-1]
        #     else:
        #         ans += c
        # return ans