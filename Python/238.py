class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftp = [1] * len(nums)
        ritp = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                leftp[i] = nums[i]
            else:
                leftp[i] = nums[i] * leftp[i - 1]
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                ritp[i] = nums[i]
            else:
                ritp[i] = nums[i] * ritp[i + 1]
        sol = [ritp[1]]
        for i in range(1, len(nums)):
            if i != len(nums) - 1:
                sol.append(leftp[i - 1] * ritp[i + 1])
            else:
                sol.append(leftp[-2])
        return sol
