# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Code Help

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i,j = 0,len(s)-1
        while i<j:
            if s[i].lower() in ['a','e','i','o','u'] and s[j].lower() in ['a','e','i','o','u']:
                s[i],s[j]=s[j],s[i]
                i = i+1
                j = j-1
            elif s[i].lower()  not in ['a','e','i','o','u'] and s[j].lower() in ['a','e','i','o','u']:
                # s[i],s[j]=s[j],s[i]
                # i = i+1
                i = i+1
            elif s[i].lower() in ['a','e','i','o','u'] and s[j].lower() not in ['a','e','i','o','u']:
                j = j-1
            else:
                i=i+1
                j = j-1
        return "".join(s)