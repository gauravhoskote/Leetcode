class Solution:

    def f(self, i, j, grid, dp):
        if (i,j) in dp:
            return dp[(i,j)]
        if i == len(grid)-1 and j == len(grid[0])-1:
            return grid[i][j]
        if i == len(grid)-1:
            dp[(i,j)] = grid[i][j] + self.f(i,j+1,grid,dp)
            return dp[(i,j)]
        if j == len(grid[0])-1:
            dp[(i,j)] = grid[i][j] + self.f(i+1,j,grid,dp)
            return dp[(i,j)]
        
        res1 = self.f(i,j+1,grid,dp)
        res2 = self.f(i+1,j,grid,dp)
        dp[(i,j)] = grid[i][j] + min(res1,res2)
        return dp[(i,j)]
        


    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        return self.f(0,0,grid, dp)
