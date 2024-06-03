class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        sol = ''
        while i < len(word):
            ii = 0
            c = word[i]
            ctr = 0
            while ii < 9 and i + ii < len(word) and word[i+ii] == c:
                ii+=1
            sol += str(ii)
            sol += c
            i += ii
        return sol
