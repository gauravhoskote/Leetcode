class Solution:    
    def addcolor(self, dd, col,ball,color):
        if ball in dd:
            col[dd[ball]] = col[dd[ball]] - 1
            if col[dd[ball]] == 0:
                del col[dd[ball]]
            dd[ball] = color
        else:
            dd[ball] = color
        col[color] = col.get(color, 0)+1
        return len(col)
    
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        col = {} #color count
        dd = {} #balls that have been colored
        sol = []
        for x,y in queries:
            sol.append(self.addcolor(dd, col, x, y))
        return sol
