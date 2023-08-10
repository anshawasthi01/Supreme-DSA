# CodeHelp
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/description/
class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] != 'a':
            return False

        st = []
        for ch in s:
            if ch == 'a':
                st.append(ch)
            elif ch == 'b':
                if st and st[-1] == 'a':
                    st.append(ch)
                else:
                    return False
            else:  # ch == 'c'
                if st and st[-1] == 'b':
                    st.pop()
                    if st and st[-1] == 'a':
                        st.pop()
                    else:
                        return False
                else:
                    return False

        return len(st) == 0  # Check if the stack is empty at the end