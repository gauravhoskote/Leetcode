class Solution:

    def f(self, s: str, t: str, i1, i2, dp):
        
        if i1== len(s):
            return True

        if i2 == len(t):
            return False
        
        if (i1,i2) in dp:
            return dp[(i1,i2)]

        if s[i1] == t[i2]:
            dp[(i1,i2)] = self.f(s,t, i1+1, i2+1,dp) or self.f(s,t,i1,i2+1,dp)
            return dp[(i1,i2)]
        else:
            dp[(i1,i2)] = self.f(s,t,i1,i2+1,dp)
            return dp[(i1,i2)]

    def isSubsequence(self, s: str, t: str) -> bool:
        dp = {}
        return self.f(s,t,0,0, dp)
