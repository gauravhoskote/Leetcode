class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            if pow(l,2)+pow(r,2) > c:
                r-=1
            elif pow(l,2)+pow(r,2) < c:
                l+=1
            else:
                return True
        return False
