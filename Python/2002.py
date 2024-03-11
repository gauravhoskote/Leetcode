class Solution:
    def f(self, s, ind, curr1, curr2):
        if ind == len(s):
            if curr1 == curr1[::-1] and curr2 == curr2[::-1]:
                return len(curr1)*len(curr2)
            else:
                return 0
        #both dont get
        r1 = self.f(s, ind+1, curr1, curr2)
        # curr 1 gets
        curr1 = curr1 + s[ind]
        # curr 2 gets
        r2 = self.f(s, ind+1, curr1, curr2)
        curr2 = curr2 + s[ind]
        curr1 = curr1[:len(curr1)-1]
        r3 = self.f(s, ind+1, curr1, curr2)
        return max(r1,r2,r3)


    def maxProduct(self, s: str) -> int:
        return self.f(s,0, "","")
