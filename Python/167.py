class Solution:

    def binary_search(self, arr, target, low=0, high=None):
        if high is None:
            high = len(arr) - 1

        while low <= high:
            mid = (low + (high-low)//2) 
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            x = self.binary_search(numbers, target-numbers[i], low = i+1)
            if x != -1:
                return [i+1, x+1]
