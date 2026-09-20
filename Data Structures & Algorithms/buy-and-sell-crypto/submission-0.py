"""
Understand:
Input: prices : list[int] where prices[i] is the price of NeetCoin on the ith day
choose a single day to buy and different day to sell
Output: max profit u can achieve
Constraints:
- choose to not make any transactions in which case profit = 0

Match - two pointers
Plan: 
- we wana buy at a low price and sell at a higher price that comes after it
l = day we buy
r = sell day
if the price at r is higher than l, we can make a profit so we update the max
if the price at r is lower, then r becomes the new l because a cheaper buying opportunity
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 #(buy day)
        r = 1 #sell day
        maxP = 0 #track max profit

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l=r
            r+=1
        return maxP
        