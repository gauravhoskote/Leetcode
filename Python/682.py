class Solution:
    def calPoints(self, operations: List[str]) -> int:
        dq = collections.deque()
        for i in range(len(operations)):
            if operations[i] == '+':
                dq.append(dq[-1]+dq[-2])
            elif operations[i] == 'D':
                dq.append(2*dq[-1])
            elif operations[i] == 'C':
                dq.pop()
            else:
                x = int(operations[i])
                dq.append(x)
        sol = 0
        for el in dq:
            sol = sol + int(el)
        return sol
