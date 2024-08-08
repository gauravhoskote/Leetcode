class Solution:

    def f(self, target, n, k, dp):
        dpi = (target, n)

        if dpi in dp:
            return dp[dpi]

        if target < 0:
            return 0

        if n == 0:
            if target == 0:
                return 1
            else:
                return 0
        
        sol = 0
        for i in range(1, k+1):
            sol += self.f(target - i, n-1, k, dp)
            sol %= 1000000007
        dp[dpi] = sol
        return dp[dpi]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        return self.f(target, n, k, dp)
