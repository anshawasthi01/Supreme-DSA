# https://leetcode.com/problems/valid-anagram/

# CodeHelp
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method 1 : Sorting
        freqTable = [0]*256
        for i in s:
            freqTable[ord(i)] += 1

        for i in range(len(t)):
            freqTable[ord(t[i])] -= 1

        for i in range(256):
            if freqTable[i] != 0:
                return False
        return True
            
