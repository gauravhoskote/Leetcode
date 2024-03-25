class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def balance(self):
        if len(self.min_heap) > 0 and len(self.max_heap)> 0 and self.min_heap[0] < -self.max_heap[0]:
            ma = -heapq.heappop(self.max_heap)
            mi = heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, ma)
            heapq.heappush(self.max_heap, -mi)

    def addNum(self, num: int) -> None:
        if len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        ma = -self.max_heap[0]
        mi = self.min_heap[0]
        if len(self.min_heap) == len(self.max_heap):
            return (mi + ma)/2
        return ma

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
