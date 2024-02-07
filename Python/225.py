class MyStack:

    def __init__(self):
        self.dq = collections.deque()

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        l = len(self.dq)-1
        for i in range(l):
            self.dq.append(self.dq[i])
        for i in range(l):
            self.dq.popleft()
        sol = self.dq[0]
        self.dq.popleft()
        return sol

    def top(self) -> int:
        sol = 0
        l = len(self.dq)-1
        for i in range(l):
            self.dq.append(self.dq[i])
        for i in range(l):
            self.dq.popleft()
        sol = self.dq[0]
        self.dq.append(self.dq[0])
        self.dq.popleft()
        return sol

    def empty(self) -> bool:
        print(self.dq)
        return len(self.dq) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
