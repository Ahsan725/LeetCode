class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) == 0 or (r,c) in seen:
                return
            seen.add((r,c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c -1))

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area 