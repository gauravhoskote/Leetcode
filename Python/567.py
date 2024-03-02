class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        sctr = Counter(s1)
        ll = len(s1)
        dd = Counter(s2[:len(s1)])
        if dd == sctr:
            return True
        n = len(s1)
        for i in range(n, len(s2)):
            dd[s2[i]] = dd.get(s2[i], 0) + 1
            dd[s2[i-n]] = dd.get(s2[i-n], 0) - 1
            if dd.get(s2[i-n]) == 0:
                dd.pop(s2[i-n])
            if dd == sctr:
                return True
        return False
