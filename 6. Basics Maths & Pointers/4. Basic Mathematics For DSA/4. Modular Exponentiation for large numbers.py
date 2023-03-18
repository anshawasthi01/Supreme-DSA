# https://practice.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers5537/1

class Solution:
	def PowMod(self, x, n, M):
		ans = 1
		while n > 0:
		    if n & 1:
		        ans = (ans * x) % M
		    
		    x = (x * x) % M
		    n >>= 1 
		    
        return ans % M
