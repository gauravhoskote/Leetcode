import bisect
class Solution:
    
    def f(self, ind, power, dd, dp, path):
        # print(path)
        # print(dp)
        dpind = (ind)
        if dpind in dp:
            return dp[dpind]
        
        if ind >= len(power):
            return 0
        path.append(power[ind])
        # take
        res1 = self.f(bisect.bisect_right(power, power[ind]+2), power, dd, dp, path) + (dd[power[ind]]*power[ind])
        path.pop()
        #not take
        res2 = self.f(bisect.bisect_right(power, power[ind]), power, dd, dp, path)
        
        dp[dpind] = max(res1, res2)
        return dp[dpind]
        
    
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        dd = Counter(power)
        dp = {}
        sol = self.f(0, power, dd, dp,[])
        return sol
