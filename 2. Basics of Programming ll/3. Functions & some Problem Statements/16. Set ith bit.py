# https://practice.geeksforgeeks.org/problems/set-kth-bit3724/1

class Solution:
	def setKthBit(self, N, K):
	    
	   # mask = 1 << K
	   # ans = N | mask
	   # return ans
	    
		return N | (1 << K)