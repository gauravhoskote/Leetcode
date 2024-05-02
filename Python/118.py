class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = [[1]]
        i = 2
        while i <= numRows:
            sol.append([])
            for j in range(i):
                if j == 0:
                    sol[-1].append(1)
                elif j == i-1:
                    sol[-1].append(1)
                else:
                    sol[-1].append(sol[-2][j]+sol[-2][j-1])
            i+=1
        return sol
