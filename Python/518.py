class Solution:
    def f(self, total, ind, coins, amount, dp):
        if total > amount:
            return 0
        if total == amount:
            return 1
        if (ind,total) in dp:
            return dp[(ind,total)]
        res = 0
        for i in range(ind, len(coins)):
            res += self.f(total + coins[i], i, coins, amount, dp)
        dp[(ind,total)] = res
        return dp[(ind,total)]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        return self.f(0,0, coins, amount, dp)
