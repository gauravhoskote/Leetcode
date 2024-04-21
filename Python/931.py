class Solution:
    
    def f(self, i, j, matrix, dp):
        if (i,j) in dp:
            return dp[(i,j)]
        
        if i == len(matrix)-1:
            return matrix[i][j]

        res1 = self.f(i+1,j, matrix, dp)
        if j + 1 < len(matrix[0]):
            res2 = self.f(i+1,j+1, matrix, dp)
        else:
            res2 = float('inf')
        if j - 1 >= 0:
            res3 = self.f(i+1,j-1, matrix, dp)
        else:
            res3 = float('inf')
        dp[(i,j)] = matrix[i][j]+min(res1,res2,res3)
        return dp[(i,j)]
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        sol = float('inf')
        dp = {}
        for i in range(len(matrix[0])):
            sol = min(sol, self.f(0,i,matrix, dp))
        return sol
