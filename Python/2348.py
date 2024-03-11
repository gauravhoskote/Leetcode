class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ctr = 0
        sol = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ctr += 1
            else:
                if ctr != 0:
                    sol += ((ctr * (ctr+1))//2)
                    ctr = 0
        if ctr != 0:
            sol += ((ctr * (ctr+1))//2)
        return sol
