class MinStack:

    def __init__(self):
        self.dq = collections.deque()
        self.ms = collections.deque()

    def push(self, val: int) -> None:
        self.dq.append(val)
        if len(self.dq)>1:
            if self.dq[-1] < self.ms[-1][0]:
                self.ms.append([self.dq[-1], len(self.dq)])
        else:
            self.ms.append([val, 1])

    def pop(self) -> None:
        if len(self.dq) == self.ms[-1][1]:
            self.ms.pop()
        self.dq.pop()

    def top(self) -> int:
        return self.dq[-1]

    def getMin(self) -> int:
        return self.ms[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
