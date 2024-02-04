class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        dt = {}
        dtn = {}
        l = 0
        p = 0
        for x in t:
            dt[x] = 1 + dt.get(x, 0)
        req = len(dt.keys())
        res_range = [-1,-1]
        res = float("infinity")
        for r in range(len(s)):
            curr = s[r]
            dtn[curr] = 1 + dtn.get(curr, 0)
            if curr in dt.keys() and dtn[curr] == dt[curr]:
                p = p + 1
            while p == req:
                if r-l+1 < res:
                    res = r-l+1
                    res_range = [l,r]
                x = s[l]
                dtn[x] = dtn[x] - 1
                if x in dt.keys() and dtn[x] < dt[x]:
                    p = p - 1
                l = l+1
        if res == float("infinity"):
            return ""
        else:
            sol = s[res_range[0] : res_range[1] + 1]
            return sol
