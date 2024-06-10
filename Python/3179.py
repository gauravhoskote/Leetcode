class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr = [1 for i in range(n)]
        mod = 1000000007
        for i in range(k):
            for j in range(1, len(arr)):
                arr[j] = (arr[j] + arr[j-1])%mod
        
        return arr[-1]
