class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        last_profit = 0
        for i in range(1, len(prices)):
            total_profit = max(last_profit, last_profit + (prices[i] - prices[i-1]))
            last_profit = total_profit
        return total_profit
