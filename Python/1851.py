import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i = 0
        hq = []
        sol = {}
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(hq, (intervals[i][1] - intervals[i][0]+1, intervals[i][1]))
                i+=1
            while hq and hq[0][1]<q:
                heapq.heappop(hq)
            if hq:
                sol[q] = hq[0][0]
            else:
                sol[q] = -1
        return [sol[q] for q in queries]
