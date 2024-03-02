class Solution:

    def incr(self, ss, tt, k, skeys):
        ss[k] = ss.get(k,0) + 1
        if ss[k] == tt[k]:
            return skeys + 1
        return skeys

    def decr(self, ss, tt, k, skeys):
        ss[k] -= 1
        if tt[k] > ss[k]:
            return skeys - 1
        return skeys

    def minWindow(self, s: str, t: str) -> str:
        tt = Counter(t)
        nkeys = len(tt.keys())
        ss = {}
        skeys = 0
        l = 0
        sol  = ''
        r = 0
        while r < len(s):
            skeys = self.incr(ss, tt, s[r], skeys)
            while skeys == nkeys:
                if sol != '':
                    if r - l < len(sol):
                        sol = s[l:r+1]
                else:
                    sol = s[l:r+1]
                skeys = self.decr(ss, tt, s[l], skeys)
                l = l + 1
            r+=1
        return sol
