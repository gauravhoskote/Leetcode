class Solution:
    def partitionString(self, s: str) -> int:
        ss = set()
        sol = 0
        for i in range(len(s)):
            if s[i] in ss:
                ss.clear()
                sol += 1
            ss.add(s[i])
        return sol+1
