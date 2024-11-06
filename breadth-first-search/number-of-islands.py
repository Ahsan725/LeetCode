class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  # If the grid is empty, return 0 islands
            return 0
        
        rows = len(grid)  # Number of rows
        cols = len(grid[0])  # Number of columns

        # Depth-First Search (DFS) to mark connected '1's as visited
        def dfs(r, c):
            # Base case: If out of bounds or water ("0"), return
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"  # Mark the current land cell as visited (turn it into water)

            # Explore the 4 neighboring directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        num_islands = 0  # Initialize the island counter

        # Iterate over every cell in the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":  # Found an unvisited island (land)
                    num_islands += 1  # Increment the island count
                    dfs(i, j)  # Perform DFS to mark the entire island
        
        return num_islands  # Return the total number of islands
