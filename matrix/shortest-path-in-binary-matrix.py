class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #bfs approach
        queue = deque([(0,0,1)])
        directions = [(0,0),(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,-1),(-1,0),]
        n = len(grid)

        if grid[0][0] or grid[-1][-1]:
            return -1
        
        while queue:
            x, y, d = queue.popleft()

            if 0<= x < n and 0 <= y < n and not grid[x][y]:
                #code here
                for x, y in directions:
                    grid[x][y] = 1
                    queue.append((x, y, d + 1))
            if x == grid[-1] and y == grid[-1]:
                return d
        return -1 
        