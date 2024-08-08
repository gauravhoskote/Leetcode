class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        mini = 10000
        minj = 10000
        maxi = -1
        maxj = -1
        flag = True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag = False
                    mini = int(min(mini, i))
                    minj = int(min(minj, j))
                    maxi = int(max(maxi, i))
                    maxj = int(max(maxj, j))
        if flag:
            return 0
        return (maxi - mini + 1)* (maxj - minj + 1)
