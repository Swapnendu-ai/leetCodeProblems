# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            maxProfit = max(maxProfit, price-minPrice)
            minPrice = min(minPrice, price)

        return maxProfit

#     def maxProfit(self, prices: List[int]) -> int:

#         maxFuturePrices = [0] * len(prices)

#         for i in range(len(prices)-2,-1,-1):
#             maxFuturePrices[i] = max(maxFuturePrices[i+1],prices[i+1])

#         return max(0,max(maxFuturePrices[i]-prices[i] for i in range(len(prices))))
