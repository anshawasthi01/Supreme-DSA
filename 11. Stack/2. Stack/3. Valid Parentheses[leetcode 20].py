# https://leetcode.com/problems/valid-parentheses/

# CodeHelp

class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for ch in s:
            # opening bracket
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            else:
                # closing bracket - ch
                if st:
                    topCh = st[-1]
                    if ch == ')' and topCh == '(':
                        # matching brackets
                        st.pop()
                    elif ch == '}' and topCh == '{':
                        # matching brackets
                        st.pop()
                    elif ch == ']' and topCh == '[':
                        # matching brackets
                        st.pop()
                    else:
                        # brackets not matching
                        return False
                else:
                    return False

        if not st:
            # valid
            return True
        else:
            return False
