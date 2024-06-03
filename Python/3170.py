import heapq
class Solution:
    
    def clearStars(self, s: str) -> str:
        hq = []
        stt = set()
        for i, ss in enumerate(s):
            if ss == '*':
                tp = heapq.heappop(hq)
                stt.add(-tp[1])
            else:
                heapq.heappush(hq, (ss,-i))
        sol = ''
        for i, ch in enumerate(s):
            if i not in stt and ch != '*':
                sol += ch
        return sol
