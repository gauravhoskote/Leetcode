class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        i = 0
        res = []
        flag = True
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                flag = False
                while i < len(intervals):
                    res.append(intervals[i])
                    i+=1
                break
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        if flag:
            res.append(newInterval)
        return res
