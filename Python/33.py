class Solution:
    def bs(self, nums, l, r, target):
        while l <= r:
            m = l + ((r - l)//2)
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mini_ind = -1
        mini = 100000
        while l <= r:
            m = l + ((r - l)//2)
            if nums[l] < nums[r]:
                if nums[m] >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            if nums[m] < mini:
                mini = nums[m]
                mini_ind = m
        if target >= mini and target <= nums[len(nums)-1]:
            return self.bs(nums, mini_ind, len(nums)-1, target)
        else:
            return self.bs(nums, 0, mini_ind-1, target)
