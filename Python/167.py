import bisect
class Solution:
    def bs(self,arr, x):
        index = bisect.bisect_left(arr, x)
        if index != len(arr) and arr[index] == x:
            return index
        else:
            return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            # print(numbers[i+1::])
            ind = self.bs(numbers[i+1::], target - numbers[i])
            # print(ind)
            if ind != -1:
                return [i+1, i+ind+2]
