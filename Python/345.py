class Solution:
    def reverseVowels(self, nums: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        nums = list(nums)
        l = 0
        r = len(nums)-1
        while l < r:
            while l<r and nums[l] not in vowels:
                l+=1
            while l<r and nums[r] not in vowels:
                r-=1
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        return ''.join(nums)
