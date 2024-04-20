class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums)-2
        while r >= 0 and nums[r] >= nums[r+1]:
            r-=1
        if r>= 0:
            last= len(nums)-1
            while nums[last]<= nums[r]:
                last-=1
            nums[r],nums[last] = nums[last],nums[r]
        nums[r+1:] = nums[r+1:][::-1]
