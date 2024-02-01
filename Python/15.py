class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums)-1
            while j < k:
                ss = nums[i] + nums[j] + nums[k]
                if ss < 0:
                    j = j + 1
                elif ss > 0:
                    k = k - 1
                else:
                    x = sorted([nums[i] , nums[j] , nums[k]])
                    sol.append(x)
                    while j < k and nums[j] == nums[j+1]:
                        j = j+ 1
                    j = j + 1
                    while j < k and nums[k] == nums[k-1]:
                        k = k- 1
                    k = k - 1

        return sol
