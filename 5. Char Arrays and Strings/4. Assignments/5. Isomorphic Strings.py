# https://leetcode.com/problems/isomorphic-strings/description/

# Code Help
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashh = [0] * 256  # mapping of each char of language 's' to language 't'
        isCharsMapped = [False] * 256 # Stores if t[i] char already mapped with s[i]

        for i in range(len(s)):
            if hashh[ord(s[i])] == 0 and not isCharsMapped[ord(t[i])]:
                hashh[ord(s[i])] = t[i]
                isCharsMapped[ord(t[i])] = True

        for i in range(len(s)):
            if hashh[ord(s[i])] != t[i]:
                return False

        return True

