class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        curr = 0
        start = 0
        for i in range(len(gas)):
            curr += (gas[i] - cost[i])
            if curr < 0:
                start = i+1
                curr = 0
        return start
