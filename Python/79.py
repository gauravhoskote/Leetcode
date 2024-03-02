class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sol = False
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def f(i, j, ii, visited):
            if i >= len(board) or i < 0 or j < 0 or j >= len(board[0]):
                return False
            if ii == len(word)-1:
                if board[i][j] != word[ii]:
                    return False
                else:
                    return True
            
            if board[i][j] != word[ii]:
                return False
            
            visited.add((i,j))
            res = False
            for dirr in directions:
                if (i + dirr[0], j + dirr[1]) not in visited:
                    res = res or f(i + dirr[0], j + dirr[1], ii+1, visited.copy())
            return res
        visited = set()
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = res or f(i,j, 0, visited.copy())
        return res
