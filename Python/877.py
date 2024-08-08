class Solution:

    def f(self, alice, asum, bsum, l, r, piles, dp):
        dpind = (l,r, alice)
        if dpind in dp:
            return dp[dpind]

        if l > r:
            return asum > bsum

        if alice:
            res1 = self.f(False, asum + piles[l], bsum, l+1, r, piles, dp)

            res2 = self.f(False, asum + piles[r], bsum, l, r-1, piles, dp)

            dp[dpind] = res1 or res2
            return dp[dpind]
        else:
            res1 = self.f(True, asum, bsum + piles[l], l+1, r, piles, dp)

            res2 = self.f(True, asum, bsum + piles[r], l, r-1, piles, dp)

            dp[dpind] = res1 or res2
            return dp[dpind]

    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        return self.f(True, 0, 0, 0, len(piles)-1, piles, dp)
