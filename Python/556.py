class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = []
        while n:
            nums.append(n%10)
            n //=10
        nums.reverse()
        r = len(nums)-2
        while r >= 0 and nums[r] >= nums[r+1]:
            r-=1
        if r>= 0:
            last= len(nums)-1
            while nums[last]<= nums[r]:
                last-=1
            nums[r],nums[last] = nums[last],nums[r]
        else:
            return -1
        nums[r+1:] = nums[r+1:][::-1]
        sol = 0
        for i in range(len(nums)):
            sol = sol * 10 + nums[i]
        
        if sol > pow(2,31)-1:
            return -1
        return sol
