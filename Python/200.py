class Solution:
    def f(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 
        if grid[i][j] == '0':
            return
        if grid[i][j] == '1':
            grid[i][j] = '0'
            dirs = [[0,1], [1,0], [0,-1], [-1,0]]
            for dirr in dirs:
                self.f(grid, i+dirr[0], j + dirr[1])
            
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        sol = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    sol += 1
                    self.f(grid, i,j)
        return sol
