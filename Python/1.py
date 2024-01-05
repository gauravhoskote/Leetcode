class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mm = {}
        for i, x in enumerate(nums):
            if target - x in mm:
                return [i, mm[target - x]]
            else:
                mm[x] = i
        return []
