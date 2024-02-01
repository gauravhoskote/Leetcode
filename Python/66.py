class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        ptr = len(digits)-1
        while carry and ptr >= 0:
            if digits[ptr] == 9:
                digits[ptr] = 0
                ptr -= 1
            else:
                digits[ptr] += 1
                carry = False
        if ptr == -1 and carry:
            digits = [1] + digits
        return digits
