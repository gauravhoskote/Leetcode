class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = k
        for num in nums:
            xor = xor ^ num
        sol = 0
        while xor:
            sol += (xor%2)
            xor //= 2
        return sol
