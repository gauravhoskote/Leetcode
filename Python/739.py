class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dq = collections.deque()
        sol = [0]*len(temperatures)
        for i in range(len(temperatures)):
            # print(dq)
            t = temperatures[i]
            if len(dq) == 0:
                dq.append([t, i])
            else:
                if t <= dq[-1][0]:
                    dq.append([t,i])
                else:
                    while len(dq) > 0 and t > dq[-1][0]:
                        sol[dq[-1][1]] = i - dq[-1][1]
                        dq.pop()
                    dq.append([t,i])
        return sol
