# https://leetcode.com/problems/minimum-cost-for-tickets/

# CodeHelp
def mincostTickets_Helper(days, costs, i):
    if i >= len(days): return 0

    # sol for a case
    # 1 Day Pass Taken
    cost1  =costs[0] + mincostTickets_Helper(days, costs, i + 1)

    # 7 Day Pass Taken
    passEndDay = days[i] + 7 - 1
    j = i
    while j < len(days) and days[j] <= passEndDay:
        j += 1
    cost7 = costs[1] + mincostTickets_Helper(days, costs, j)

    # 30 Day Pass Taken
    passEndDay = days[i] + 30 - 1
    j = i
    while j < len(days) and days[j] <= passEndDay:
        j += 1
    cost30 = costs[2] + mincostTickets_Helper(days, costs, j)

    return min(cost1, cost7, cost30)

class Solution:
    def mincostTickets(self, days, costs):
        return mincostTickets_Helper(days, costs, 0)