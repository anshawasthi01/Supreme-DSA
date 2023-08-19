# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# CodeHelp

def maxProfitFinder(prices, i, minPrice, maxProfit):
    if i == len(prices): return

    if prices[i] < minPrice[0]: 
        minPrice[0] = prices[i]

    todayProfit = prices[i] - minPrice[0]
    
    if todayProfit > maxProfit[0]: 
        maxProfit[0] = todayProfit

    # RE
    maxProfitFinder(prices, i+1, minPrice, maxProfit)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # Iterative
        # maxprofit=0
        # minpricetillnow=9999999999
        # for price in prices:
        #     maxprofit=max(maxprofit,price-minpricetillnow)
        #     minpricetillnow=min(minpricetillnow, price)
        # return maxprofit
        minPrice = [9999999]
        maxProfit = [0]
        maxProfitFinder(prices, 0, minPrice, maxProfit)
        return maxProfit[0]

        