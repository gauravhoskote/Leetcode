class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        md = float('inf')
        for i in range(1,len(arr)):
            md = min(md, arr[i]-arr[i-1])
        sol = []
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] == md:
                sol.append([arr[i-1],arr[i]])
        return sol
