class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def condition(hsum):
            csum = 0
            cnt=1
            for i in range(len(nums)):
                csum += nums[i]
                if csum > hsum:
                    csum = nums[i]
                    cnt += 1
                    if cnt > k:
                        return False
            return True
        l = max(nums)
        r = sum(nums)
        while l < r:
            m = l + (r-l)//2
            print(m)
            if condition(m):
                r = m
            else:
                l = m + 1
        return l
