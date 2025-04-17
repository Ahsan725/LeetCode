class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid) #because it is a square matric n * n

        def out_of_bounds(r,c):
            if r < 0 or c < 0 or r >= N or c >= N:
                return True

        def dfs(r,c, label):
            if out_of_bounds(r,c) or grid[r][c] != 1:
                return 0
            grid[r][c] = label 
            size = 1
            dirs = [[r+1,c], [r-1,c], [r, c-1], [r, c+1]]
            for nr, nc in dirs:
                size += dfs(nr, nc, label)
            return size

        #1. Precompute areas
        size = defaultdict(list) #island label -> size 
        label = 2 #starting from a value that wont clash with input 0 or 1
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                   size[label] = dfs(r,c, label)
                   label += 1

        def connect(r,c):
            dirs = [[r+1,c], [r-1,c], [r, c-1], [r, c+1]]
            visit = set()
            res = 1
            for nr, nc in dirs:
                if not out_of_bounds(nr, nc) and grid[r][c] not in visit:
                    res += size[grid[nr][nc]] 
                    visit.add(grid[nr][nc])
            return res 

        #2 Try Flipping water cell to find the one that will give the most area
        res = 0 if not size else max(size.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    res = max(res, connect(r,c))
        return res 

