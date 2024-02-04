class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        mm = prices[0]
        for i in range(1, len(prices)):
            curr = prices[i] - mm
            sol = max(sol, curr)
            mm = min(prices[i], mm)
        return sol
