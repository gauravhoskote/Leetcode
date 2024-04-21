class Solution:

    def f(self, nums):
        # print(len(nums))
        if len(nums) <= 2:
            if nums[0]>nums[-1]:
                nums[0],nums[-1] = nums[-1],nums[0]
            return nums
        
        mid = len(nums)//2

        res = []
        nums1 = self.f(nums[:mid+1])
        nums2 = self.f(nums[mid+1:])
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1+=1
            else:
                res.append(nums2[p2])
                p2+=1
        while p1<len(nums1):
            res.append(nums1[p1])
            p1+=1
        
        while p2<len(nums2):
            res.append(nums2[p2])
            p2+=1
        
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.f(nums)
