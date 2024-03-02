class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lm = height[l]
        rm = height[r]
        sol = 0
        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                sol += lm-height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                sol += rm-height[r]
        return sol
