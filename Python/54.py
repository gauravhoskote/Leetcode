class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rlimit = len(matrix[0])
        llimit = -1
        ulimit = -1
        dlimit = len(matrix)
        i = 0
        j = 0
        sol = []
        flag = True
        while(True):
            # go right
            flag = True
            while(j < rlimit):
                flag = False
                sol.append(matrix[i][j])
                j = j + 1
            if flag:
                break
            ulimit = ulimit + 1
            j = j - 1
            i = i + 1

            # go down
            flag = True
            while(i < dlimit):
                flag = False
                sol.append(matrix[i][j])
                i = i + 1
            if flag:
                break
            rlimit = rlimit - 1
            i = i - 1
            j = j - 1

            # go left
            flag = True
            while(j > llimit):
                flag = False
                sol.append(matrix[i][j])
                j = j - 1
            if flag:
                break
            
            dlimit = dlimit - 1
            j = j + 1
            i = i - 1

            # go up
            flag = True
            while(i > ulimit):
                flag = False
                sol.append(matrix[i][j])
                i = i - 1
            if flag:
                break
            
            llimit = llimit + 1
            i = i + 1
            j = j + 1
        return sol
