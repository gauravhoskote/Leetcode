class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(speed) == 0:
            return 0
        ps = []
        for i in range(len(position)):
            ps.append((position[i], speed[i]))
        ps.sort()
        st = []
        sol = 0
        pos = ps[-1]
        for i in reversed(range(len(ps)-1)):
            p = ps[i]
            t = (target - p[0])/p[1]
            t_top = (target - pos[0])/pos[1]
            if t > t_top:
                pos= p
                sol+=1
        return sol+1
