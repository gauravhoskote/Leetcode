class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ml = 0
        for num in s:
            if num - 1 not in s:
                l = 1
                while num + 1 in s:
                    num = num + 1
                    l = l + 1
                ml = max(ml, l)
        return ml
