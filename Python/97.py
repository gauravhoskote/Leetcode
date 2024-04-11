class Solution:

    def f(self, i1, i2, i3, s1, s2, s3, dp):
        if (i1,i2) in dp:
            return dp[(i1,i2)]
        if i3 == len(s3) and (i1 != len(s1) or i2 != len(s2)):
            return False
        if i1 == len(s1) and i2 == len(s2):
            return i3 == len(s3)
        if i1 == len(s1):
            return s2[i2] == s3[i3] and self.f(i1,i2+1,i3+1,s1,s2,s3, dp)
        if i2 == len(s2):
            return s1[i1] == s3[i3] and self.f(i1+1,i2,i3+1,s1,s2,s3, dp)
        
        r1 = s1[i1] == s3[i3] and self.f(i1+1,i2,i3+1,s1,s2,s3, dp)
        r2 = s2[i2] == s3[i3] and self.f(i1,i2+1,i3+1,s1,s2,s3, dp)
        dp[(i1,i2)] = r1 or r2
        return dp[(i1,i2)]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        dp = {}
        return self.f(0,0,0,s1,s2,s3, dp)
