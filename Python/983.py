import bisect
class Solution:
    
    def f(self, i, days, costs, dp):
        if i == len(days):
            return 0
        
        if i in dp:
            return dp[i]

        index1 = bisect.bisect_left(days, days[i]+1)
        res1 = costs[0] + self.f(index1, days, costs, dp)

        index2 = bisect.bisect_left(days, days[i]+7)
        res2 = costs[1] + self.f(index2, days, costs, dp)

        index3 = bisect.bisect_left(days, days[i]+30)
        res3 = costs[2] + self.f(index3, days, costs, dp)

        dp[i] = min(res1,res2,res3)
        return dp[i]
    
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        return self.f(0,days,costs, dp)
