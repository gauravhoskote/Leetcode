class Solution:
    
    def maximalSquare(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                   grid[i][j] = 1
                else:
                    grid[i][j] = 0
        sol = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i > 0 and j > 0:
                        grid[i][j] = max(grid[i][j], 1 + min(grid[i-1][j], grid[i][j-1], grid[i-1][j-1]))
                        sol = max(sol, grid[i][j] * grid[i][j])
                    else:
                        sol = max(sol,1)
        return sol
