class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d1 = {}
        for i in range(len(s1)):
            d1[s1[i]] = 1 + d1.get(s1[i], 0)
        d2 = {}
        for i in range(len(s1)):
            d2[s2[i]] = 1 + d2.get(s2[i], 0)
        if len(s1) == len(s2):
            return d1 == d2
        if d1 == d2:
            return True
        l = 0
        for i in range(len(s1), len(s2)):
            d2[s2[i]] = 1 + d2.get(s2[i], 0)
            d2[s2[l]] = d2[s2[l]] - 1
            if d2[s2[l]] == 0:
                d2.pop(s2[l])
            l += 1
            if d1 == d2:
                return True
        return False
