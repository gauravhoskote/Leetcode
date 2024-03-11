class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        for i, layer in enumerate(wall):
            s = 0
            new_layer = []
            for brick in layer:
                s += brick
                new_layer.append(s)
            wall[i] = new_layer
        print(wall)
        gaps = {}
        max_gaps = 1
        for layer in wall:
            for i, gap in enumerate(layer):
                if i != len(layer)-1:
                    gaps[gap] = gaps.get(gap, 0) + 1
                    if gaps[gap] > max_gaps:
                        max_gaps = gaps[gap]
        if len(gaps.keys()) == 0:
            return len(wall)
        return len(wall) - max_gaps
