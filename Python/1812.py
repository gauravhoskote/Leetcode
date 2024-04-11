class Solution:
    def squareIsWhite(self, c: str) -> bool:
        p1 = int(ord(c[0]) - ord('a'))
        p2 = int(ord(c[1]) - ord('1'))
        if (p1%2 == 0 and p2%2 == 0) or (p1%2 == 1 and p2%2 == 1):
            return False
        else:
            return True
