class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        dirr = 1
        ii =0
        for i in range(k):
            if ii == 0:
                dirr = 1
            elif ii == n-1:
                dirr = -1
            ii += dirr
        return ii
