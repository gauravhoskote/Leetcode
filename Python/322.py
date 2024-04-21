class Solution:
    def f(self, coins, curr, dp):
        if curr == 0:
            return 0
        if curr in dp:
            return dp[curr]
        dp[curr] = float('inf')
        for coin in coins:
            if curr - coin >= 0:
                dp[curr] = min(1 + self.f(coins,curr-coin,dp), dp[curr])
        return dp[curr]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        res = self.f(coins, amount, dp)
        if res == float('inf'):
            return -1
        return res
