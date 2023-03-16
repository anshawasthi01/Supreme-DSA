# https://leetcode.com/problems/reverse-only-letters/

# CodeHelp

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        l, h = 0, len(s)-1
        s = list(s)

        while l < h:
            if s[l] in chars:
                if s[h] in chars:
                    s[l], s[h] = s[h], s[l]
                    l += 1
                    h -= 1
                else:
                    h -= 1
            else:
                l += 1
        return ''.join(s)

