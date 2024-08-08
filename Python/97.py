class Solution:
    def f(self,i1,i2,i3,s1,s2,s3,dp):
        dpind = (i1,i2)
        if dpind in dp:
            return dp[dpind]

        if i3 == len(s3):
            return True
        if i1 != len(s1) and i2 != len(s2):
            if s1[i1] != s3[i3] and s2[i2] != s3[i3]:
                return False
            else:
                if s1[i1] == s3[i3] and s2[i2] == s3[i3]:
                    dp[dpind] = self.f(i1+1,i2,i3+1,s1,s2,s3,dp) or self.f(i1,i2+1,i3+1,s1,s2,s3,dp)
                    return dp[dpind]
                else:
                    if s1[i1] == s3[i3]:
                        dp[dpind] = self.f(i1+1,i2,i3+1,s1,s2,s3,dp)
                        return dp[dpind]
                    else:
                        dp[dpind] = self.f(i1,i2+1,i3+1,s1,s2,s3,dp)
                        return dp[dpind]
        else:
            if i2 == len(s2):
                dp[dpind] = s1[i1] == s3[i3] and self.f(i1+1,i2,i3+1,s1,s2,s3,dp)
                return dp[dpind]
            else:
                dp[dpind] = s2[i2] == s3[i3] and self.f(i1,i2+1,i3+1,s1,s2,s3,dp)
                return dp[dpind]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        dp = {}
        return self.f(0,0,0,s1,s2,s3,dp)
