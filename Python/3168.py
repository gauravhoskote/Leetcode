class Solution:
    def minimumChairs(self, s: str) -> int:
        ctr = 0
        sol = 0
        for ss in s:
            if ss == 'E':
                ctr +=1
            else:
                ctr-=1
            sol = max(sol, ctr)
        return sol
