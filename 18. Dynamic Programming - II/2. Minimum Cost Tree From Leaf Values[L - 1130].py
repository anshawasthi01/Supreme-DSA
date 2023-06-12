# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/

# CodeHelp

from typing import List
from collections import defaultdict

class Solution:
    def solveUsingRecursion(self, arr: List[int], maxi: defaultdict, left: int, right: int) -> int:
        # base case
        if left == right:
            return 0

        ans = float('inf')

        for i in range(left, right):
            ans = min(ans, 
                      maxi[(left,i)] * maxi[(i+1, right)] 
                      + self.solveUsingRecursion(arr, maxi, left, i)
                      + self.solveUsingRecursion(arr, maxi, i+1, right))
        return ans

    def solveUsingMem(self, arr: List[int], maxi: defaultdict, left: int, right: int, dp: List[List[int]]) -> int:
        # base case
        if left == right:
            return 0

        if dp[left][right] != -1:
            return dp[left][right]

        ans = float('inf')

        for i in range(left, right):
            ans = min(ans, 
                      maxi[(left,i)] * maxi[(i+1, right)] 
                      + self.solveUsingMem(arr, maxi, left, i, dp)
                      + self.solveUsingMem(arr, maxi, i+1, right, dp))
        dp[left][right] = ans
        return dp[left][right]

    def solveUsingTab(self, arr: List[int], maxi: defaultdict) -> int:
        n = len(arr)
        dp = [[0] * (n+1) for _ in range(n+1)]

        for left in range(n-1, -1, -1):
            for right in range(n):
                if left >= right:
                    continue
                else:
                    # valid range
                    ans = float('inf')

                    for i in range(left, right):
                        ans = min(ans, 
                                  maxi[(left,i)] * maxi[(i+1, right)] 
                                  + dp[left][i]
                                  + dp[i+1][right])
                    dp[left][right] = ans

        return dp[0][n-1]

    def mctFromLeafValues(self, arr: List[int]) -> int:
        maxi = defaultdict(int)
        
        # pre-computation   
        for i in range(len(arr)):
            maxi[(i,i)] = arr[i]
            for j in range(i+1, len(arr)):
                maxi[(i,j)] = max(arr[j], maxi[(i,j-1)])

        n = len(arr)
        # ans = self.solveUsingRecursion(arr, maxi, 0, n-1)

        # dp = [[-1] * (n+1) for _ in range(n+1)]
        # ans = self.solveUsingMem(arr, maxi, 0, n-1, dp)

        ans = self.solveUsingTab(arr, maxi)
        return ans
