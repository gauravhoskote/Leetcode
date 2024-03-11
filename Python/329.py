class Solution:
    def check(self,i, j, matrix):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return False
        return True
    
    def f(self, i, j, matrix, last, dp):
        if matrix[i][j] <= last:
            return 0
        if (i,j) in dp:
            return dp[(i,j)]
        res = 0
        last = matrix[i][j]
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dirr in dirs:
            if self.check(i+dirr[0], j+dirr[1], matrix):
                res = max(res, self.f(i+dirr[0], j+dirr[1],matrix,last, dp))
        
        dp[(i,j)] = 1 + res
        return 1 + res

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sol = 1
        dp = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[(i,j)] = self.f(i,j,matrix,-1, dp)
                sol = max(sol, dp[(i,j)])
        return sol
