class Solution:
    def f(self, i, j, dp, text1, text2):
        
        if i >= len(text1) or j >= len(text2):
            return 0
        if (i,j) in dp:
            return dp[(i,j)]
        if text1[i] == text2[j]:
            dp[(i,j)] = 1 + self.f(i+1,j+1, dp, text1, text2)
            return dp[(i,j)]
        else:
            dp[(i,j)] = max(self.f(i,j+1, dp, text1, text2), self.f(i+1,j, dp, text1, text2))
            return dp[(i,j)]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        return self.f(0,0,dp,text1, text2)
