class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = {}
        mc = 0
        l = 0
        sol = 0
        for r in range(len(s)):
            f[s[r]] = 1 + f.get(s[r], 0)
            mc = max(mc, f[s[r]])
            if (r - l + 1) - mc > k:
                f[s[l]] -= 1
                l += 1
            else:
                sol = max(sol, (r - l + 1))
        return sol
