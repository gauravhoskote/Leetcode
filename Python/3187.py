class segment_tree:

    def __init__(self, a, func):
        self.a = a
        self.t = [0]*(4*len(a))
        self.dd = {}
        self.func = func
        self.build(1, 0, len(self.a)-1)

    def getrange(self, v, tl, tr, l, r):
        if l > r:
            return 0
        elif tl == l and tr == r:
            return self.t[v]
        else:
            tm = (tl + tr)//2
            return self.getrange(v*2, tl, tm, l, min(r,tm)) + self.getrange(v*2 + 1, tm+1, tr, max(tm+1, l), r)

    def build(self, v, tl, tr):
        if tl == tr:
            self.dd[tl] = v
            if tl == 0 or tl == len(self.a)-1:
                self.t[v] = 0
            else:
                if self.a[tl] > self.a[tl-1] and self.a[tl] > self.a[tl+1]:
                    self.t[v] = 1
                else:
                    self.t[v] = 0
        else:
            tm = (tl + tr)//2
            self.build(v*2, tl, tm)
            self.build(v*2+1, tm+1, tr)
            self.t[v] = self.t[v*2] + self.t[v*2+1]
            

    def update_element(self, v, newval, pos, tl, tr):
        if tl == tr:
            if tl == 0 or tl == len(self.a)-1:
                self.t[v] = 0
            else:
                if self.a[tl] > self.a[tl-1] and self.a[tl] > self.a[tl+1]:
                    self.t[v] = 1
                else:
                    self.t[v] = 0
        else:
            tm = (tl + tr)//2
            if tm >= pos:
                self.update_element(2*v, newval, pos, tl, tm)
            else:
                self.update_element(2*v+1, newval, pos, tm+1, tr)
            self.t[v] = self.t[v*2] + self.t[v*2+1]
    
    
    def get_range(self, l,r):
        return self.getrange(1, 0, len(self.a)-1, l, r)

    
    def update(self, index, newval):
        self.a[index] = newval
        self.update_element(1, newval, index, 0, len(self.a)-1)
        self.update_element(1, newval, index-1, 0, len(self.a)-1)
        self.update_element(1, newval, index+1, 0, len(self.a)-1)


        
        
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        stree = segment_tree(nums, max)
        sol = []
        for q in queries:
            if q[0] == 1:
                sol.append(stree.get_range(q[1]+1,q[2]-1))
            else:
                stree.update(q[1],q[2])
        
        return sol
