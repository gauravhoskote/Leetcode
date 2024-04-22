class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {}
        for edge in edges:
            if edge[0] in adj:
                adj[edge[0]].append(edge[1])
            else:
                adj[edge[0]] = [edge[1]]
            
            if edge[1] in adj:
                adj[edge[1]].append(edge[0])
            else:
                adj[edge[1]] = [edge[0]]
            
        visited = set()
        dq = deque()
        dq.append(source)
        while dq:
            ne = dq[0]
            if ne == destination:
                return True
            visited.add(ne)
            dq.popleft()
            for neighbor in adj[ne]:
                if neighbor not in visited:
                    dq.append(neighbor)
        return False
