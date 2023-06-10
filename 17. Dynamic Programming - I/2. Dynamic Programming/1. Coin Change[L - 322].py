# CodeHelp
# https://leetcode.com/problems/coin-change/
    
class Solution:
    def solveUsingRecursion(self, coins, amount):
        # Base case
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')

        mini = float('inf')
        for i in range(len(coins)):
            ans = self.solveUsingRecursion(coins, amount - coins[i])
            if ans != float('inf'):
                mini = min(mini, 1 + ans)
        
        return mini


    def solveMem(self, coins, amount, dp):
        # Base case
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        
        # Check if answer already exists
        if dp[amount] != -1:
            return dp[amount]

        mini = float('inf')
        for i in range(len(coins)):
            ans = self.solveMem(coins, amount - coins[i], dp)
            if ans != float('inf'):
                mini = min(mini, 1 + ans)

        dp[amount] = mini
        return dp[amount]


    def solveTab(self, coins, amount):
        # Step 1: Create dp array
        dp = [float('inf')] * (amount + 1)
        # Step 2: Base case
        dp[0] = 0
        # Step 3: Top-down approach flow and code
        for target in range(1, amount + 1):
            mini = float('inf')
            for i in range(len(coins)):
                if target - coins[i] >= 0:
                    ans = dp[target - coins[i]]
                    if ans != float('inf'):
                        mini = min(mini, 1 + ans)
                    
            dp[target] = mini
        
        return dp[amount]


    def coinChange(self, coins: List[int], amount: int) -> int:
        # ans = self.solveUsingRecursion(coins, amount)
        # if ans == float('inf'):
        #     return -1
        # else:
        #     return ans

        # dp = [-1] * (amount + 1)
        # ans = self.solveMem(coins, amount, dp)
        # if ans == float('inf'):
        #     return -1
        # else:
        #     return ans

        ans = self.solveTab(coins, amount)
        if ans == float('inf'):
            return -1
        else:
            return ans
