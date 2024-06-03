import bisect
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        arr = []
        for i in range(len(nums)-1):
            if (nums[i]+nums[i+1])%2 == 0:
                arr.append(i)
        sol = []
        for q in queries:
            l1 = bisect.bisect_left(arr, q[0])
            l2 = bisect.bisect_left(arr, q[1])
            if l1 == l2:
                sol.append(True)
            else:
                sol.append(False)
        
        return sol
