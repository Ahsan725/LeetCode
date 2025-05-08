class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #two parts: dfs, itertaive part 
        rows = len(grid)
        cols = len(grid[0])
        res = 0


        #dfs 
        def dfs(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == '0':
                return 
            grid[r][c] = '0'

            dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in dirs:
                dfs(r + dr, c + dc)


        #iterative 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r,c)
        return res 
