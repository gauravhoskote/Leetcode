class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.dp = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.dp[grid[i][j]] = (i,j)
        
    def adjacentSum(self, value: int) -> int:
        i,j = self.dp[value]
        i1 = i + 1 if i < len(self.grid)-1 else -1
        i2 = i - 1 if i > 0 else -1
        j1 = j + 1 if j < len(self.grid[0])-1 else -1
        j2 = j - 1 if j > 0 else -1

        sol = 0
        if i1 != -1:
            sol+= self.grid[i1][j]
        if i2 != -1:
            sol+= self.grid[i2][j]
        if j1 != -1:
            sol+= self.grid[i][j1]
        if j2 != -1:
            sol+= self.grid[i][j2]
        return sol
        

    def diagonalSum(self, value: int) -> int:
        i,j = self.dp[value]
        i1 = i + 1 if i < len(self.grid)-1 else -1
        i2 = i - 1 if i > 0 else -1
        j1 = j + 1 if j < len(self.grid[0])-1 else -1
        j2 = j - 1 if j > 0 else -1

        sol = 0
        if i1 != -1 and j1 != -1:
            sol+= self.grid[i1][j1]
        if i2 != -1 and j1 != -1:
            sol+= self.grid[i2][j1]
        if j2 != -1 and i1 != -1:
            sol+= self.grid[i1][j2]
        if j2 != -1 and i2 != -1:
            sol+= self.grid[i2][j2]
        return sol
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
