class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r,c, seen_set, prevh):
            if ((r,c) in seen_set or r < 0 or r >= rows or c < 0  or c >= cols or heights[r][c] < prevh):
                return 
            seen_set.add((r,c))
            dfs(r + 1,c, seen_set, heights[r][c])
            dfs(r - 1,c, seen_set, heights[r][c])
            dfs(r,c + 1, seen_set, heights[r][c])
            dfs(r,c - 1, seen_set, heights[r][c])
        
        
        for r in range(rows): 
            dfs(r,0, pac, heights[r][0]) #first row touching pac
            dfs(r,cols-1, atl, heights[r][cols-1]) #last row touchinf atl

        for c in range(cols): 
            dfs(0,c, pac, heights[0][c]) #first col touching pac
            dfs(rows - 1 ,c, atl, heights[rows-1][c]) #last col touchinf atl

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c]) 
        return res