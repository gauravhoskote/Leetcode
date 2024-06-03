class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        sol = 0
        sol += max(0, meetings[0][0] - 1)
        rm = meetings[0][1]
        for i in range(len(meetings)-1):
            sol += max(0, meetings[i+1][0] - rm - 1)
            rm = max(rm, meetings[i+1][1])
        sol += max(0, days - rm)
        return sol
