from collections import defaultdict
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def out_of_bounds(r, c):
            return r < 0 or c < 0 or r >= N or c >= N

        def dfs(r, c, label):
            if out_of_bounds(r, c) or grid[r][c] != 1:
                return 0
            grid[r][c] = label
            size = 1
            for nr, nc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                size += dfs(nr, nc, label)
            return size

        # Step 1: Label each island with unique number and record its size
        size = defaultdict(int)
        label = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    label += 1

        def connect(r, c):
            seen = set()
            total = 1  # start with 1 for the flipped 0
            for nr, nc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                if not out_of_bounds(nr, nc) and grid[nr][nc] > 1 and grid[nr][nc] not in seen:
                    seen.add(grid[nr][nc])
                    total += size[grid[nr][nc]]
            return total

        # Step 2: Try flipping each 0 to 1 and find max connected area
        res = max(size.values(), default=0)  # in case grid has no 0s
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    res = max(res, connect(r, c))

        return res
