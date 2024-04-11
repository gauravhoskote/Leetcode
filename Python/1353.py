class Solution:
    def maxEvents(self, nums: List[List[int]]) -> int:
        nums.sort(key = lambda x : tuple(x))
        pq = []
        start = nums[0][0]
        sol = 0
        i = 0
        mm = float('-inf')
        for num in nums:
            mm = max(mm, num[1])
        while start <= mm:
            while i < len(nums) and nums[i][0] <= start:
                heapq.heappush(pq, nums[i][1])
                i+=1
            while len(pq)> 0 and pq[0] < start:
                heapq.heappop(pq)
            if len(pq)>0:
                heapq.heappop(pq)
                sol += 1
            start += 1
        return sol
