# https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1

#User function Template for python3

class Solution:
    def gcd(self, A, B):
        if A == 0: return B
        if B == 0: return A
        
        while A > 0 and B > 0:
            if A > B:
                A = A - B
            else:
                B = B - A
        
        return B if A == 0 else A