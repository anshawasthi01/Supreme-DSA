# https://leetcode.com/problems/palindromic-substrings/

# CodeHelp
def expandAroundIndex(s, left, right):
        count = 0
        # jab tak match karega, tab tak count increment kardo and i piche and j aaage kardo
        while(left >= 0 and right <len(s) and s[left] == s[right] ):
            count += 1
            left -= 1
            right += 1
        return count
    
class Solution:
    def countSubstrings(self, s: str) -> int:
        totalCount = 0
        n = len(s)

        for center in range(n):
            # odd
            oddKaAns = expandAroundIndex(s, center, center)
            totalCount = totalCount + oddKaAns
            # even
            evenKaAns = expandAroundIndex(s,center,center+1)
            totalCount = totalCount + evenKaAns

        return totalCount
    




