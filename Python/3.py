class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        l = 0
        ss = set()
        sol = 0
        curr = 0
        for r in range(len(nums)):
            curr += 1
            while nums[r] in ss:
                curr-=1
                ss.remove(nums[l])
                l+=1
            ss.add(nums[r])
            sol = max(sol, r-l+1)
        return sol
