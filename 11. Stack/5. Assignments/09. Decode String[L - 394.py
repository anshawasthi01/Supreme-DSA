# https://leetcode.com/problems/decode-string/description/
# CodeHelpA

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == ']':
                stringToRepeat = ""
                while st and st[-1] != "[":
                    top = st.pop()
                    stringToRepeat += top
                st.pop()
                numericTimes = ""
                while st and st[-1].isdigit():
                    numericTimes += st.pop()
                numericTimes = numericTimes[::-1]
                n = int(numericTimes)

                # final decoding
                current_decode = ""
                while n > 0:
                    current_decode += stringToRepeat
                    n -= 1
                st.append(current_decode)
            else:
                st.append(ch)

        ans = ""
        while st:
            ans += st.pop()
        return ans[::-1]