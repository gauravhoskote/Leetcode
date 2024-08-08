class Solution:

    def f(self, i1, i2, s, dp):
        dpind = (i1,i2)
        if dpind in dp:
            return dp[dpind]

        if i1>i2:
            return 0

        if i1 == i2:
            return 1
        else:
            if s[i1] == s[i2]:
                dp[dpind] = 2 + self.f(i1+1, i2-1, s, dp)
                return dp[dpind]
            else:
                dp[dpind] = max(self.f(i1+1, i2, s, dp), self.f(i1, i2-1, s, dp))
                return dp[dpind]

    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        return self.f(0,len(s)-1, s, dp)
