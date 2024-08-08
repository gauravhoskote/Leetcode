class Solution:


    def f(self, i1, i2, w1, w2, dp):
        dpi = (i1,i2)
        if dpi in dp:
            return dp[dpi]

        if i1 == len(w1) or i2 == len(w2):
            if i1 == len(w1):
                return len(w2) - i2
            else:
                return len(w1) - i1

        if w1[i1] == w2[i2]:
            dp[dpi] = self.f(i1+1, i2+1, w1, w2, dp)
            return dp[dpi]
        else:
            # insert
            res1 = self.f(i1, i2+1, w1, w2, dp)
            # replace
            res2 = self.f(i1+1, i2+1, w1, w2, dp)
            # delete
            res3 = self.f(i1+1, i2, w1, w2, dp)

            dp[dpi] = 1+ min(res1, res2, res3)
            return dp[dpi]

    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        return self.f(0,0,word1,word2,dp)
