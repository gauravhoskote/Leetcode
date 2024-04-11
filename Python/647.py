class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        sol = 0
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for j in range(1, n):
            ii = 0
            jj = j
            while jj < n:
                if abs(ii-jj) == 1:
                    if s[ii] == s[jj]:
                        dp[ii][jj] = 1
                else:
                    if s[ii] == s[jj]:
                        dp[ii][jj] = dp[ii+1][jj-1]
                jj+=1
                ii+=1
        sol = [sum(el) for el in dp]
        return sum(sol)
