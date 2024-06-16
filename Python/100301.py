class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        dd = {}
        for i,h in enumerate(hours):
            hours[i] = h%24
        # print(hours)
        sol = 0
        for i in range(len(hours)):
            if (24 - hours[i])%24 in dd:
                sol += (dd[(24 - hours[i])%24])
            dd[hours[i]] = dd.get(hours[i], 0)+1
        return sol
