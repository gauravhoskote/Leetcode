class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for el in nums:
            if el in s:
                return True
            else:
                s.add(el)
        return False
