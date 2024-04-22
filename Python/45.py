class Solution:    
    def jump(self, nums: List[int]) -> int:
        arr = [float('inf')]*len(nums)
        arr[0] = 0
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i+j < len(nums):
                    arr[i+j] = min(arr[i]+1, arr[i+j])
        return arr[-1]
