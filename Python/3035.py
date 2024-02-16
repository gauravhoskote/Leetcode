class Solution:    
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        dd = Counter([w for word in words for w in word])
        npairs = 0
        for k in dd.keys():
            npairs += (dd[k]//2)
        sol = 0
        for s in sorted([len(word) for word in words]):
            npairs = npairs - s//2
            if npairs >= 0:
                sol += 1
        return sol
