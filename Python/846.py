import heapq
class Solution:
    def f(self, hq, dd, el,groupSize):
        diff = dd[el]
        for i in range(groupSize):
            if el + i in dd:
                dd[el+i] -= diff
                if dd[el+i] < 0:
                    return False
                if dd[el+i] == 0:
                    if hq[0] == el+i:
                        heapq.heappop(hq)
                        del dd[el+i]
                    else:
                        return False
            else:
                return False
        return True

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        dd = Counter(hand)
        hq = list(set(hand))
        heapq.heapify(hq)
        
        while hq:
            top = hq[0]
            if not self.f(hq,dd,top,groupSize):
                return False
        return True
