class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
        if len(matrix) > 1:
            for i in range(1, len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 1:
                        matrix[i][j] = matrix[i][j] + matrix[i-1][j]
        
        sol = 0
        for i in range(len(matrix)):
            matrix[i].append(0)
            dq = collections.deque()
            for j in range(len(matrix[i])):
                while len(dq)>0 and matrix[i][j] < matrix[i][dq[-1]]:
                    x = matrix[i][dq[-1]]
                    dq.pop()
                    if len(dq)>0:
                        left = dq[-1]
                    else:
                        left = -1
                    sol = max(sol, (j - 1 - left)*x)
                dq.append(j)
        print(matrix)
        return sol
