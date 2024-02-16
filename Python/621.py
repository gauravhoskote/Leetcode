class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dd = Counter(tasks)
        hq = [-el for el in dd.values()]
        heapq.heapify(hq)
        time = 0
        q = deque()
        while hq or q:
            time += 1
            if hq:
                cnt = 1 + heapq.heappop(hq) 
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(hq, q[0][0])
                q.popleft()
        return time
