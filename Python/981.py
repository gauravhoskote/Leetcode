class TimeMap:

    def __init__(self):
        self.d= {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.d.get(key) == None:
            self.d[key] = [[timestamp, value]]
        else:
            self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if self.d.get(key) == None:
            return ''
        matrix = self.d[key]
        l = 0
        r = len(matrix) - 1
        sol = -1
        m = l + ((r - l)//2)
        while l <= r:
            m = l + ((r - l)//2)
            if matrix[m][0] <= timestamp:
                l = m +1
                sol = m
            else:
                r = m-1
        if sol == -1:
            return ''
        return matrix[sol][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
