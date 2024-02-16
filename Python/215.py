class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        sol = ''
        for i in range(k):
            sol = heapq.heappop(nums)
        return -sol
