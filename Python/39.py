class Solution:
    
    def f(self, ind, candidates, target, csum, csol, sol):
        print(csol)
        if csum == target:
            sol.append(csol.copy())
            return
        if csum > target or ind >= len(candidates):
            return
        
        csol.append(candidates[ind])
        self.f(ind, candidates, target, csum+ candidates[ind], csol, sol)
        csol.pop()
        self.f(ind+1, candidates, target, csum, csol, sol)
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        self.f(0,candidates, target, 0, [], sol)
        return sol
