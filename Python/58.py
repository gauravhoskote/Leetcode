class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        sol = []
        for el in arr:
            if el != '':
                sol.append(el)
        return len(sol[-1])
