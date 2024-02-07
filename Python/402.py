class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        dq = collections.deque()
        for i in range(len(num)):
            x = int(num[i])
            while len(dq)>0 and x < dq[-1] and k > 0:
                dq.pop()
                k -= 1
            dq.append(x)
        while len(dq) and k > 0:
            dq.pop()
            k -= 1
        t = 1
        sol = '0'
        if len(dq) == 0:
            return str(sol)
        for i in range(len(dq)):
            sol += str(dq[i])
        
        si = 0
        print(sol)
        while si < len(sol) and sol[si] == '0' :
            si += 1
        return  sol[si:] if si < len(sol) else '0'
