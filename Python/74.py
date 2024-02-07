class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) * len(matrix[0])
        l, r = 0, n-1
        while l <= r:
            m = l + ((r - l) // 2)
            i = m // len(matrix[0])
            j = m % len(matrix[0])
            if matrix[i][j] > target:
                r = m-1
            elif matrix[i][j] < target:
                l = m+1
            else:
                return True
        return False
