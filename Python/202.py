class Solution:

    def get_sum_of_sq_of_digits(self, n):
        s = 0
        while(n):
            x = n % 10
            s = s + (x**2)
            n = n // 10
        return s

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.get_sum_of_sq_of_digits(n)
        while(slow != fast):
            print('slow = ' + str(slow))
            print('fast = ' + str(fast))
            if fast == 1:
                return True
            slow = self.get_sum_of_sq_of_digits(slow)
            fast = self.get_sum_of_sq_of_digits(self.get_sum_of_sq_of_digits(fast))
        return True if fast == 1 else False
