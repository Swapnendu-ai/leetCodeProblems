# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if len(prices) < 2:
            return result

        minTillNow = prices[0]

        for price in prices[1:]:
            result = max(result,price-minTillNow)
            minTillNow = min(minTillNow,price)

        return result
