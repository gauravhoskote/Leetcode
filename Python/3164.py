class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        dd = {}
        for i in range(len(nums2)):
            dd[nums2[i]*k] = 1 + dd.get(nums2[i]*k, 0)
        
        sol = 0
        for i in range(len(nums1)):
            for j in range(1, math.floor(math.sqrt(nums1[i]))+1):
                if nums1[i]%j == 0 and (j in dd or nums1[i]/j in dd):
                    if j in dd:
                        sol += dd[j]
                    if nums1[i]/j in dd:
                        sol += dd[nums1[i]/j]
                    if j == nums1[i]/j:
                        sol -= dd[j]
                    
            # print(sol)
        return sol
