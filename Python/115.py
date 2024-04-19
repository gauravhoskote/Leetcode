class Solution:
    
    def f(self, i, j, s, t, dp):
        if (i,j) in dp:
            return dp[(i,j)]
        if i >= len(s) or j >= len(t):
            if i >= len(s) and j >= len(t):
                return 1
            if i >= len(s):
                return 0
            return 1

        if s[i] == t[j]:
            res1 = self.f(i+1, j+1, s, t, dp)
            res2 = self.f(i+1, j, s, t, dp)
            dp[(i,j)] = res1 + res2
            return dp[(i,j)]
        else:
            dp[(i,j)] = self.f(i+1, j, s, t, dp)
            return dp[(i,j)]

    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        return self.f(0,0,s,t, dp)
