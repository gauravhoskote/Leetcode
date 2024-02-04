class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        sol = []
        for r in range(len(nums)):
            if len(dq) > 0 and dq[0] < r - k + 1: # change this
                dq.popleft()
            while len(dq) > 0 and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            if r >= k-1:
                sol.append(nums[dq[0]])
        return sol
