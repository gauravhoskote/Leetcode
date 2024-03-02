class Solution:

    def f(self, n, carr, sol, visited, nums):
        print(carr)
        print(visited)
        if len(carr) == n:
            sol.append(carr.copy())
            return
        
        for i in range(n):
            if i not in visited:
                carr.append(nums[i])
                visited.add(i)
                self.f(n,  carr.copy(), sol, visited.copy(), nums)
                carr.pop()
                visited.remove(i)
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol = []
        visited = set()
        self.f(n, [], sol, visited, nums)
        return sol
