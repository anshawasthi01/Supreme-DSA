# https://leetcode.com/problems/minimum-window-substring/description/
# CodeHelp

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, p: str) -> str:
        len1 = len(s)
        len2 = len(p)
        start = 0
        ansIndex = -1
        ansLen = float('inf')

        if len1 < len2:
            return ""

        strMap = defaultdict(int)
        patMap = defaultdict(int)

        # to keep track of all characters of P string
        for ch in p:
            patMap[ch] += 1

        count = 0

        for i in range(len1):
            ch = s[i]
            strMap[ch] += 1

            # valid character -> jo character tumhare opattern me bhi ho 
            if strMap[ch] <= patMap[ch]:
                count += 1

            if count == len2:
                # Window is ready

                # minimise the window -> freq decrement, ans update , start ko aage badhana h 
                while strMap[s[start]] > patMap[s[start]] or patMap[s[start]] == 0:
                    if strMap[s[start]] > patMap[s[start]]:
                        strMap[s[start]] -= 1
                    start += 1

                # Update answer
                lengthOfWindow = i - start + 1
                if lengthOfWindow < ansLen:
                    ansLen = lengthOfWindow
                    ansIndex = start

        if ansIndex == -1:
            return ""
        else:
            return s[ansIndex:ansIndex + ansLen]




        # d=Counter(t)
        # c=len(d)
        # i=start=0
        # n=len(s)
        # ans=n+1
        # for j in range(n):
        #     if s[j] in d:
        #         d[s[j]]-=1
        #         if d[s[j]]==0:
        #             c-=1            
        #     while c==0:
        #         if ans>j-i+1:
        #             ans=j-i+1
        #             start=i
        #         if s[i] in d:
        #             d[s[i]]+=1
        #             if d[s[i]]>0:
        #                 c+=1
        #         i+=1
        # if ans>n:
        #     return ""
        # return s[start:start+ans]