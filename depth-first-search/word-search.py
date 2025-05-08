class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #mostly the same structure as a regaulr dfs problem 
        rows = len(board)
        cols = len(board[0])
        path = set()

        #dfs
        def dfs(r, c, i):
            if r < 0 or c < 0 or r >= rows or c >= cols or i >= len(word) or board[r][c] != word[i] or (r,c) in path:
                return False 
            if i == len(word) - 1:
                return True 
            
            path.add((r,c))
            res = dfs(r + 1,c, i + 1) or dfs(r - 1,c, i + 1) or dfs(r,c + 1, i + 1) or dfs(r,c - 1, i + 1)
            path.remove((r,c))
            return res 



        #iterative 
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True 
        return False 