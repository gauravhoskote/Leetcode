class Solution:
    def isValid(self, i, j, heights):
        if i >= 0 and j >= 0 and i < len(heights) and j < len(heights[0]):
            return True
        return False

    def pacific(self, i, j, heights, visited):
        if i == 0 or j == 0:
            return True
        
        res = False
        visited.add((i,j))
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        for dirr in dirs:
            if self.isValid(i + dirr[0], j + dirr[1], heights) and heights[i + dirr[0]][j + dirr[1]] <= heights[i][j] and (i + dirr[0], j + dirr[1]) not in visited:
                res = res or self.pacific(i + dirr[0], j + dirr[1], heights, visited.copy())
        visited.remove((i,j))
        return res

    def atlantic(self, i, j, heights, visited):
        if i == len(heights)-1 or j == len(heights[0])-1:
            return True

        res = False
        visited.add((i,j))
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        for dirr in dirs:
            if self.isValid(i + dirr[0], j + dirr[1], heights) and heights[i + dirr[0]][j + dirr[1]] <= heights[i][j] and (i + dirr[0], j + dirr[1]) not in visited:
                res = res or self.atlantic(i + dirr[0], j + dirr[1], heights, visited.copy())
        visited.remove((i,j))
        return res
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        sol = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visited = set()
                if self.pacific(i,j, heights, visited) and self.atlantic(i,j, heights, visited):
                    sol.append([i,j])
        return sol
