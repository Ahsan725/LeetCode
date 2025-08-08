class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Understanding: we are counting islands and everytime we see a connected island that is counted as 1 
        #Approch: iterate over matrix and anytime we see a '1' we want to call a dfs function to mark all connected islands as just one island. so we don;t over count
        
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        
        def dfs(r,c):
            #check boundaries and base condition
            if r >= rows or c >= cols or r<0 or c<0 or grid[r][c] == '0':
                return 
            #marking 
            grid[r][c] = '0'
            
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r,c)
        return res 