class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for src, dst, wt in edges:
            adj[src].append([dst,wt])
            adj[dst].append([src,wt])
        
        # print(adj)
        
        shortest = {}
        pq = [(0,0)]
        # print('START LOOP')
        while pq:
            mm = heapq.heappop(pq)
            
            cdist,node = mm[0],mm[1]
            # print("NODE: "+str(node))
            # print('DIST: '+str(cdist))
            if node in shortest:
                continue
            shortest[node] = cdist
            # print('NEIGHBORS')
            # print(adj[node])
            for e in adj[node]:
                nn = e[0]
                wtt = e[1]
                if nn not in shortest:
                    heapq.heappush(pq,(cdist+wtt,nn))
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        ##################################
        
        shortest2 = {}
        pq = [(0,n-1)]
        # print('START LOOP')
        while pq:
            mm = heapq.heappop(pq)
            
            cdist,node = mm[0],mm[1]
            # print("NODE: "+str(node))
            # print('DIST: '+str(cdist))
            if node in shortest2:
                continue
            shortest2[node] = cdist
            # print('NEIGHBORS')
            # print(adj[node])
            for e in adj[node]:
                nn = e[0]
                wtt = e[1]
                if nn not in shortest2:
                    heapq.heappush(pq,(cdist+wtt,nn))
        
        for i in range(n):
            if i not in shortest2:
                shortest2[i] = -1
        ##################################
        sdist = shortest[n-1]
        sol = []
        # print(shortest)
        # print(shortest2)
        
        for i in range(len(edges)):
            en1 = edges[i][0]
            en2 = edges[i][1]
            ewt = edges[i][2]
            if (ewt + shortest[en1]+shortest2[en2]  == sdist and (shortest[en1]!=-1) and (shortest2[en2]!=-1) ) or (ewt + shortest[en2]+shortest2[en1] == sdist and (shortest[en2]!=-1) and (shortest2[en1]!=-1)):
                sol.append(True)
            else:
                sol.append(False)
        return sol
