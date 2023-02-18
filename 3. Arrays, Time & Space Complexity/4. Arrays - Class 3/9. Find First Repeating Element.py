# https://practice.geeksforgeeks.org/problems/first-repeating-element4018/1

#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,a, n):
        mp = {}
        for i in range(len(arr)):
            if a[i] in mp:
                mp[a[i]] += 1 # In Cpp use only this line
            else:
                mp[a[i]] = 1
            
        for i in range(n):
            if mp[a[i]] > 1:
                return i+1
        return -1