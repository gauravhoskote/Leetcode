class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1.copy()
        B = nums2.copy()
        
        if len(A) > len(B):
            A,B = B,A
        
        total = len(A) + len(B)
        half = total //2
        l =0
        r = len(A)-1
        while True:
            i = (l + r)//2
            j = half - i - 2

            aleft = A[i] if i >= 0 else float('-inf')
            aright = A[i+1] if i+1 < len(A) else float('inf')
            bleft = B[j] if j >= 0 else float('-inf')
            bright = B[j+1] if j+1 < len(B) else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                else:
                    return (min(aright, bright) + max(aleft, bleft))/2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1
