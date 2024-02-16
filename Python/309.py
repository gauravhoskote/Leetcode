class Solution:
    def f(self, ind, task, prices, dp):
        if ind >= len(prices):
            return 0
        if (ind, task) in dp:
            return dp[(ind,task)]
        if task == 'buy':
            if ind < len(prices)-1:
                dp[(ind,task)] = max((self.f(ind+1, 'sell', prices, dp) - prices[ind]), self.f(ind+1, 'buy', prices, dp))
                return dp[(ind,task)]
            else:
                return 0
        else:
            dp[(ind,task)] = max((prices[ind] + self.f(ind+2, 'buy', prices, dp)) , self.f(ind+1, 'sell', prices, dp))
            return dp[(ind,task)]
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        return self.f(0, 'buy', prices, dp)
