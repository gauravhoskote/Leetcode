class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]
        sol = 0
        if len(intervals) <= 1:
            return 0
        i = 1
        print(intervals)
        while i < len(intervals):
            if end > intervals[i][0]:
                if end > intervals[i][1]:
                    end = intervals[i][1]
                    sol += 1
                else:
                    sol+=1
            else:
                end = intervals[i][1]
            i+= 1
        return sol
