import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i] = [points[i][0]**2 + points[i][1]**2, points[i]]
        print(points)
        heapq.heapify(points)
        k_smallest = heapq.nsmallest(k, points)
        print(k_smallest)
        sol = []
        for k in k_smallest:
            sol.append(k[1])
        return sol
