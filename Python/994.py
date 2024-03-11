class Solution:
    
    def isValid(self, i, j, heights):
        if i >= 0 and j >= 0 and i < len(heights) and j < len(heights[0]):
            return True
        return False

    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        visited = set()
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dq.append((i,j))
                    visited.add((i,j))
        
        sol = -1
        while len(dq):
            print(dq)
            ctr = len(dq)
            while ctr>0:
                (i, j) = dq.popleft()
                for dirr in dirs:
                    if self.isValid(i + dirr[0], j + dirr[1], grid) and (i + dirr[0], j + dirr[1]) not in visited and grid[i + dirr[0]][j+dirr[1]] == 1:
                        dq.append((i + dirr[0], j + dirr[1]))
                        visited.add((i + dirr[0], j + dirr[1]))
                        grid[i + dirr[0]][j+dirr[1]] = 2

                ctr = ctr -1
            sol += 1
        
        print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        if sol == -1:
            return 0
        return sol
