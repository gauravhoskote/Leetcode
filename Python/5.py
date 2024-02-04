class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        dp = [[False] * len(s) for _ in range(len(s))]
        # print(dp)
        for i in range(len(s)):
            dp[i][i] = True
        # print(dp)
        for c in range(1, len(s)):
            i = 0
            j = c
            while i < len(s) and j < len(s):
                if s[i] == s[j]:
                    if j == i+1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                i += 1
                j += 1
        sol_len = 0
        sol_range = [-1,-1]
        # print(dp)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j-i+1 > sol_len and dp[i][j]:
                    sol_len = j-i+1
                    sol_range = [i,j]
        return s[sol_range[0]: sol_range[1]+1]
