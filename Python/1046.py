import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        print(stones)
        if len(stones) == 1:
            return stones[0]
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            l1 = heapq.heappop(stones)
            l2 = heapq.heappop(stones)
            # print(l1)
            # print(l2)
            if l1 != l2:
                heapq.heappush(stones, -abs(l1 - l2))
                # print(-abs(l1 - l2))
        if len(stones):
            return -stones[0]
        return 0
