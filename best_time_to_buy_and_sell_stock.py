from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, maximum_profit = prices[0], 0
        for price in prices:
            maximum_profit = max(maximum_profit, price - min_price)
            min_price = min(min_price, price)
        return maximum_profit