class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(val):
            ctr = val
            sol =1
            for x in weights:
                if ctr < x:
                    sol +=1
                    ctr = val - x
                else:
                    ctr -= x
            return sol <= days
        
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = l + (r-l)//2
            if condition(m):
                r = m
            else:
                print(2)
                l = m + 1
        return l
