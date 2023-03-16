# https://leetcode.com/problems/valid-palindrome-ii/

# CodeHelp

def checkPalindrome(s, i, j):
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<=j:
            if s[i] != s[j]:
                # ek baar i ko remove, ek baar j ko remove
                return checkPalindrome(s,i+1, j) or checkPalindrome(s, i, j-1)
            else:
                # s[i] == s[j]
                i += 1
                j -= 1
        return True




