class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        mm = {}
        for el in strs:
            print(el)
            m = {}
            for c in el:
                if c not in m:
                    m[c] = 1
                else:
                    m[c] = m[c] + 1
            skeys = sorted(m.keys())
            sm = {i: m[i] for i in skeys}
            print(str(sm))
            if str(sm) in mm:
                mm[str(sm)].append(el)
            else:
                mm[str(sm)] = [el]
        for k, v in mm.items():
            sol.append(v)
        return sol
