class Solution:
    def perf_op(self,operator, op1, op2):
        op1 = int(op1)
        op2 = int(op2)
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        if operator == '*':
            return op1 * op2
        if operator == '/':
            return int(op1 / op2)

    def evalRPN(self, tokens: List[str]) -> int:
        ind  = len(tokens)-1
        operators = ['+','-','/','*']
        dq = collections.deque()
        for t in tokens:
            if t in operators:
                op1 = dq[-2]
                op2 = dq[-1]
                dq.pop()
                dq.pop()
                dq.append(str(self.perf_op(t, op1, op2)))
            else:
                dq.append(t)
        return int(dq[0])


