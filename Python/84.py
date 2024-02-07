class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        dq = collections.deque()
        sol = 0
        for i,h in enumerate(heights):
            while len(dq)>0 and h < heights[dq[-1]]:
                x = heights[dq[-1]]
                dq.pop()
                if len(dq)>0:
                    left = dq[-1]
                else:
                    left = -1
                sol = max(sol, (i-left-1)*x)
            dq.append(i)
        return sol
