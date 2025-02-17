class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicates( block: List[str]) -> bool:
        # Check if there are any duplicate numbers in the block
            return len(block) != len(set(block))
        # Check all rows
        for i in range(9):
            seen = set() #create a set for O(1) lookups
            for j in range(9):
                if board[i][j] in seen: #if it has been seen before means invalid
                    return False
                elif board[i][j] != '.': #if it is a new number and also not a blank cell add it to seen
                    seen.add(board[i][j])

        # Check all columns
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen: #just flip i,j to j,i
                    return False
                elif board[j][i] != '.':
                    seen.add(board[j][i])

        # Check all 3x3 sub-grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_grid = []
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != '.':
                            sub_grid.append(board[x][y])
                if has_duplicates(sub_grid):
                    return False

        # If no duplicates found, the Sudoku is valid
        return True


