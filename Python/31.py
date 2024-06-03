class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return 
        i = len(nums)-2
        j = len(nums)-1

        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        
        if i>=0:
            while j > i and nums[i]>= nums[j]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        j = len(nums)-1
        i+=1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
