class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 1:
            return profit 
        s, f = 0, 1
        while s < len(prices) - 1:
            profit = max(profit, prices[f] - prices[s])
            f += 1
            if f == len(prices):
                s += 1
                f = s + 1
        return profit