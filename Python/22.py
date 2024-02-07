class Solution:
    def f(self, sol, s,e,cs, n):
        if s == n and e == n:
            sol.append(cs)
        if s < n:
            self.f(sol, s+1, e, cs+'(', n)
        if e < n and e < s:
            self.f(sol, s, e+1, cs+')', n)

    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        self.f(sol, 0,0,'', n)
        return sol
