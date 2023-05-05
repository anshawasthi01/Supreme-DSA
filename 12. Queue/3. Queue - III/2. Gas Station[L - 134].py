# https://leetcode.com/problems/gas-station/

# CodeHelp
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # kitna petrol kam padgya
        deficit = 0
        # kitna petrol bacha hua h 
        balance = 0
        # circuit kaha se start krre ho
        start = 0

        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                # yahi pr galti hogi
                deficit += abs(balance)
                start = i+1
                balance = 0

        if balance >= deficit:
            return start
        else:
            return -1
