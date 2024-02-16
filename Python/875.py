class Solution:
    def f(self, k, piles):
        h = 0
        for pile in piles:
            h += pile//k
            if pile%k != 0:
                h += 1
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        print(piles)
        l = 1
        r = max(piles)
        sol = r
        while l < r:
            m = l + ((r - l)//2)
            th = self.f(m, piles)
            print(th)
            if th > h:
                l = m+1
            elif th <= h:
                r = m
                sol = min(sol,m)
        return sol
