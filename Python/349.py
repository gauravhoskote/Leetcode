class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        sol = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                sol.append(nums1[i])
                x = nums1[i]
                while i < len(nums1) and nums1[i] == x:
                    i+=1
                while j < len(nums2) and  nums2[j] == x:
                    j+=1
        return sol
