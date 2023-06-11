# https://practice.geeksforgeeks.org/problems/painting-the-fence3727/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# CodeHelp

class Solution:
    def solveUsingRecursion(self, n, k):
        if n == 1:
            return k
        if n == 2:
            return k + k * (k - 1)

        ans = (self.solveUsingRecursion(n - 2, k) + self.solveUsingRecursion(n - 1, k)) * (k - 1)
        return ans

    def solveUsingMem(self, n, k, dp):
        if n == 1:
            return k
        if n == 2:
            return k + k * (k - 1)

        if dp[n] != -1:
            return dp[n]

        dp[n] = (self.solveUsingMem(n - 2, k, dp) + self.solveUsingMem(n - 1, k, dp)) * (k - 1)
        return dp[n]

    def solveUsingTab(self, n, k):
        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k + k * (k - 1)

        for i in range(3, n + 1):
            dp[i] = (dp[i - 2] + dp[i - 1]) * (k - 1)
    
        return dp[n]

    def solveSO(self, n, k):
        prev2 = k
        prev1 = (k + k * (k - 1))

        for i in range(3, n + 1):
            curr = (prev2 + prev1) * (k - 1)
            # shhift -> yaha hi galti karunga ya karungi 
            prev2 = prev1
            prev1 = curr
    
        return prev1
    
    def countWays(self,n,k):
        # ans = self.solveUsingRecursion(n, k)

        # dp = [-1] * (n + 1)
        # ans = self.solveUsingMem(n, k, dp)

        # ans = self.solveUsingTab(n, k)
        
        ans = self.solveSO(n, k)
        return ans