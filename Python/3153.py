class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        arr = [[] for j in range(len(nums))]
        # print(arr)
        for i, num in enumerate(nums):
            while num:
                arr[i].append(num%10)
                num //= 10
        # print(arr)
        solm = [[0 for i in range(10)]for j in range(len(arr[0]))]
        # print(solm)
        for j in range(len(arr[0])):
            for i in range(len(arr)):
                solm[j][arr[i][j]]+=1
        # print(solm)
        
        sol =0
        for s in solm:
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    sol += (s[i]*s[j])
        
        return sol
