class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ms = {}
        mt = {}
        for i, ch in enumerate(s):
            if ch not in ms:
                ms[ch] = 1
            else:
                ms[ch] = ms[ch] + 1
            ch = t[i]
            if ch not in mt:
                mt[ch] = 1
            else:
                mt[ch] = mt[ch] + 1
        for k, v in ms.items():
            if k in ms and k in mt:
                if ms[k] != mt[k]:
                    return False
            else:
                return False
        return True
