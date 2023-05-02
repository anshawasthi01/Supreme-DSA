# https://leetcode.com/problems/longest-valid-parentheses/description/

# Code Help

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        max_len = 0
        
        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    length = i - st[-1]
                    max_len = max(max_len, length)
                    
        return max_len
