class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        x = nums[0]
        ctr = 1
        for i in range(1, len(nums)):
            if x == nums[i]:
                ctr += 1
            else:
                ctr -= 1
                if ctr < 0:
                    x = nums[i]
                    ctr = 1
        return x
