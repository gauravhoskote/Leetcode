class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fd = {}
        for num in nums:
            if num in fd.keys():
                fd[num] = fd[num]+1
            else:
                fd[num] = 1
        arr = ['0']* len(nums)
        for key, v in fd.items():
            if arr[v-1] == '0':
                arr[v-1] = [key]
            else:
                arr[v-1].append(key)
        sol = []
        for i in reversed(range(len(nums))):
            if len(sol) == k:
                break
            if arr[i] != '0':
                sol = sol + arr[i]
        return sol
