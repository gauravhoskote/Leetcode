class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        sol = []
        for i in range(len(nums)):
            while dq and dq[-1][1] <= nums[i]:
                dq.pop()
            dq.append((i,nums[i]))
            if i >= k-1:
                sol.append(dq[0][1])
            if i-(k-1) == dq[0][0]:
                dq.popleft()
        return sol
