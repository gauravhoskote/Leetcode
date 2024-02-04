class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        left = 0
        right = 0
        cs = 0
        sol = 0
        while right < len(s):
            if s[right] in ss:
                while s[left] != s[right]:
                    ss.remove(s[left])
                    left += 1
                    cs -= 1
                left += 1
                right += 1
                # remove all elements that are in the set until we reach s[i]
            else:
                #add the element to the set and move forward
                ss.add(s[right])
                cs = cs + 1
                if cs > sol:
                    sol = cs
                right += 1
        return sol
