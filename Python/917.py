class Solution:

    def isletter(self, c):
        if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            return True

    def reverseOnlyLetters(self, nums: str) -> str:
        nums = list(nums)
        l = 0
        r = len(nums)-1
        while l < r:
            while l < r and not self.isletter(nums[l]):
                l+=1
            while l < r and not self.isletter(nums[r]):
                r-=1
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        return ''.join(nums)
