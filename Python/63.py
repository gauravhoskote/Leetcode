class Solution:
    
    def f(self, m, n, grid, dp):
        dpind = (m,n)
        if dpind in dp:
            return dp[dpind]

        if m == len(grid)-1 and n == len(grid[0])-1:
            return 1 if grid[m][n] == 0 else 0

        if grid[m][n] == 0:
            if m == len(grid)-1 or n == len(grid[0])-1:
                if m == len(grid)-1:
                    dp[dpind] = self.f(m, n+1, grid, dp)
                    return dp[dpind]
                else:
                    dp[dpind] = self.f(m+1, n, grid, dp)
                    return dp[dpind]
            dp[dpind] = self.f(m, n+1, grid, dp) + self.f(m+1, n, grid, dp)
            return dp[dpind]
        else:
            return 0

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        return self.f(0,0,obstacleGrid, dp)
