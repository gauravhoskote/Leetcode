class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x : x[1], reverse=True)
        sol = 0
        for el in boxTypes:
            sol = sol + (el[1]* min(truckSize, el[0]))
            truckSize = max(0, truckSize - el[0])
        return sol
