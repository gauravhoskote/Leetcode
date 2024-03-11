class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        flag = False
        while l < r:
            if s[l] != s[r]:
                break
            l += 1
            r -= 1
        left = s[l:r]
        right = s[l+1:r+1]
        res1 = left == left[::-1]
        res2 = right == right[::-1]
        return res1 or res2
