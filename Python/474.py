class Solution:
    
    def f(self, m,n,mp,i, dp):
        dpi = (i, m, n)
        
        if dpi in dp:
            return dp[dpi]

        if m < 0 or n < 0:
            return 0
        
        if i in mp:
            z = mp[i][0]
            o = mp[i][1]
            sol = float('-inf')
            if m - z >= 0 and n - o >= 0:
                sol = max(sol, 1 + self.f(m-z,n-o,mp, i+1, dp))
            sol = max(sol, self.f(m,n,mp, i+1, dp))
            dp[dpi] = sol
            return dp[dpi]
        else:
            return 0
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mp = {}
        for i in range(len(strs)):
            s = strs[i]
            z = 0
            o = 0
            for j in s:
                if j == '0':
                    z+=1
                else:
                    o+=1
            mp[i] = (z,o)
        print(mp)
        dp = {}
        return self.f(m, n, mp, 0, dp)
