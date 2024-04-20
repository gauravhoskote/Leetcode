class Solution:
    def reverseString(self, nums: List[str]) -> None:
        l = 0
        r = len(nums)-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
