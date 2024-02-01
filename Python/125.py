class Solution:
    def isPalindrome(self, s: str) -> bool:
        for c in s:
            if not (c.isalpha() or c.isdigit()):
                s = s.replace(c, '')
            else:
                s = s.replace(c, c.lower())
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
