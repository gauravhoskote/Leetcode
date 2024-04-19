class Solution:
    def reorganizeString(self, s: str) -> str:
        hq = []
        ctr = Counter(s)
        for k,v in ctr.items():
            heapq.heappush(hq, (-v, k))
        
        sol = ""
        while hq:
            print(hq)
            top = heapq.heappop(hq)
            if len(sol) == 0:
                print('1')
                sol = sol + top[1]
                if top[0]+1 != 0:
                    heapq.heappush(hq, (top[0]+1, top[1]))
            else:
                if top[1] == sol[-1]:
                    print('2')
                    if hq:
                        top2 = heapq.heappop(hq)
                        sol = sol + top2[1]
                        heapq.heappush(hq, top)
                        if top2[0]+1 != 0:
                            heapq.heappush(hq, (top2[0]+1, top2[1]))
                    else:
                        print('3')
                        return ""
                else:
                    print('4')
                    sol = sol + top[1]
                    if top[0]+1 != 0:
                        heapq.heappush(hq, (top[0]+1, top[1]))
        return sol
