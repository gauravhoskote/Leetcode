class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ge = -1
        sol = []
        for i in reversed(range(len(arr))):
            sol.append(ge)
            ge = max(ge,arr[i])
        return reversed(sol)
