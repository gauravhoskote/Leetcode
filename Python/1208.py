class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        cc = 0
        sol = 0
        for r in range(min(len(s), len(t))):
            cc += (abs( ord(s[r]) - ord(t[r]) ))
            while cc > maxCost:
                cc -= (abs( ord(s[l]) - ord(t[l])))
                l+=1
            sol = max(sol, (r-l+1))
        return sol
