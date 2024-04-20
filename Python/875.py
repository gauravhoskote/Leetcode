class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(val):
            cnt = 0
            for i in range(len(piles)):
                cnt += piles[i]//val
                if piles[i]%val:
                    cnt+=1
                if cnt > h:
                    return False
            return True

        l = 1
        r = max(piles)

        while l < r:
            m = l + (r-l)//2
            if condition(m):
                r = m
            else:
                l = m+1
        return l
