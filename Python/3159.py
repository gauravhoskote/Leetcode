class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        dd = {}
        ctr = 1
        for i, num in enumerate(nums):
            if num == x:
                dd[ctr] = i
                ctr+=1
        sol = []
        for q in queries:
            if q in dd:
                sol.append(dd[q])
            else:
                sol.append(-1)
        return sol
