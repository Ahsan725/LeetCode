class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #create variables to help
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == 'O' or r == rows -1 or c == cols -1:
                return 
            # board[r][c] = 'X'
            
            dfs(r + 1,c)
            dfs(r,c + 1)
            dfs(r - 1,c)
            dfs(r,c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    dfs(r,c) 
                    
        
                    
        