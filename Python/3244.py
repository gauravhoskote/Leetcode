from sortedcontainers import SortedList
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        sl = SortedList([i for i in range(n)])
        sol = []
        for q in queries:
            u = q[0]
            v = q[1]
            ind1 = sl.bisect_left(u) + 1
            ind2 = sl.bisect_left(v)
            diff = ind2 - ind1
            for i in range(diff):
                sl.pop(ind1)
            sol.append(len(sl)-1)
        return sol
