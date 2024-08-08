class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        def f(i, j, dp):
            dpi = (i,j)
            if dpi in dp:
                return dp[dpi]
            
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]

            sol = float('inf')
            
            if i + 1 < len(grid):
                sol = min(sol, grid[i][j] + f(i+1, j, dp))
            
            if j + 1 < len(grid[0]):
                sol = min(sol, grid[i][j] + f(i, j+1, dp))
            
            dp[dpi] = sol
            return dp[dpi]
        
        return f(0,0, dp)
