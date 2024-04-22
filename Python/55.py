class Solution:
    def canJump(self, nums: List[int]) -> bool:
        highest = 0
        for i, num in enumerate(nums):
            if i > highest:
                break
            highest = max(highest,i + num)
            if highest >= len(nums)-1:
                return True
        return False
