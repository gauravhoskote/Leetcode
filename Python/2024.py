class Solution:
    def maxConsecutiveAnswers(self, nums: str, k: int) -> int:
        l = 0
        sol = 0
        nf = 0
        for r in range(len(nums)):
            if nums[r] == 'F':
                nf += 1
            mm = min(nf, r-l+1-nf)
            while mm > k:
                if nums[l] == 'F':
                    nf -= 1
                l+=1
                mm = min(nf, r-l+1-nf)
            sol = max(sol, r-l+1)
        return sol
