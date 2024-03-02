class Solution:
    def f(self, i, j, grid, vis):
        if (i,j) in vis:
            return 0
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 0
        
        if grid[i][j] == 0:
            return 0
        
        if grid[i][j] == 1:
            dirs = [[0,1], [1,0], [0,-1], [-1,0]]
            sol = 1
            vis.add((i,j))
            for dirr in dirs:
                sol += self.f(i+dirr[0], j + dirr[1], grid, vis)
            return sol

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sol = 0
        vis = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sol = max(sol, self.f(i,j,grid, vis))
        return sol
