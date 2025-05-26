from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1: Add all rotten oranges to queue and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh += 1
        
        # Step 2: BFS to rot adjacent fresh oranges
        time = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            r, c, mins = q.popleft()
            time = max(time, mins)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, mins + 1))

        # Step 3: Check if any fresh oranges remain
        return time if fresh == 0 else -1
