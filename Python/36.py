class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        j = 0
        for i in range(0, 9, 3):
            for j in range(0,9,3):
                ss = set()
                for ii in range(i, i+3):
                    for jj in range(j, j+3):
                        if board[ii][jj] != '.':
                            if board[ii][jj] not in ss:
                                ss.add(board[ii][jj])
                                # print('added : ' + str(board[ii][jj]))
                            else:
                                print(1)
                                # print(i)
                                # print(j)
                                # print(board[ii][jj])
                                return False
        for i in range(9):
            ss = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in ss:
                        ss.add(board[i][j])
                    else:
                        print(2)
                        return False
        for j in range(9):
            ss = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in ss:
                        ss.add(board[i][j])
                    else:
                        print(3)
                        return False
        return True
