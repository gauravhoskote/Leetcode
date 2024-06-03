class Solution:
    
    def f(self, i, jump, k, last, dp):
        if jump > 0 and i-k > 1:
            return 0
        if (i, jump, last) in dp:
            return dp[(i, jump, last)]
        sol = 0
        if i == k:
            sol += 1
        
        if last == 0 and i != 0:
            sol += self.f(i-1, jump, k, 1, dp)
        
        sol += self.f(i+(2**jump), jump + 1, k, 0, dp)
        
        dp[(i, jump, last)] = sol
        return sol
        
    
    def waysToReachStair(self, k: int) -> int:
        dp = {}
        return self.f(1,0,k,0,dp)
