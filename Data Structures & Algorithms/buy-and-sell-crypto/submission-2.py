class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 1:
            return profit 
        l, r = 0, 1
        while l < len(prices) - 1:
            profit = max(profit, prices[r] - prices[l])
            r += 1
            if r == len(prices):
                l += 1
                r = l + 1
        return profit