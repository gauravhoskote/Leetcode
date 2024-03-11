class Solution:
    
    def mark_first_island(self, i, j, grid, dq):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        
        if grid[i][j] == 0 or grid[i][j] == -1:
            return
        
        if grid[i][j] == 1:
            grid[i][j] = -1
            dq.append((i,j))

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dirr in dirs:
            self.mark_first_island(i+dirr[0], j+dirr[1], grid, dq)

    
    def check(self,i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return False
        return True

    def shortestBridge(self, grid: List[List[int]]) -> int:
        dq = deque()
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    print('HI')
                    self.mark_first_island(i, j, grid, dq)
                    flag = True
                    break
            if flag:
                break
        sol = 0
        print(grid)
        while len(dq):
            ctr = len(dq)
            print(dq)
            while ctr > 0:
                ctr -= 1
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                (i,j) = dq.popleft()
                for dirr in dirs:
                    if self.check(i + dirr[0], j + dirr[1], grid) and grid[i + dirr[0]][j + dirr[1]] == 1:
                        return sol
                    if self.check(i + dirr[0], j + dirr[1], grid) and grid[i + dirr[0]][j + dirr[1]] == 0:
                        grid[i + dirr[0]][j + dirr[1]] = -1
                        dq.append((i + dirr[0], j + dirr[1]))
            sol += 1
        return sol
