# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# CodeHelp
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n-m+1):
            for j in range(m):
                if needle[j] != haystack[i+j]:
                    break

                if j== m-1:
                    return i
        return -1
                