class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        t_prices = [float('inf')]*n
        adj = {}
        for s,d,p in flights:
            if s not in adj:
                adj[s] = [(d,p)]
            else:
                adj[s].append((d,p))
        prices[src] = 0
        t_prices[src] = 0
        ss = set()
        ts = set()
        ss.add(src)
        for i in range(k+1):
            ts.clear()
            for s in ss:
                if s in adj:
                    for ed in adj[s]:
                        d = ed[0]
                        p = ed[1]
                        if prices[s] != float('inf') and prices[s] + p < t_prices[d]:
                            t_prices[d] = prices[s] + p
                            ts.add(d)
            for d in ts:
                prices[d] = t_prices[d]
            ss = ts.copy()
        return -1 if prices[dst] == float('inf') else prices[dst]
