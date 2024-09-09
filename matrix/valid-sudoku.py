class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicates( block: List[str]) -> bool:
        # Check if there are any duplicate numbers in the block
            return len(block) != len(set(block))
        # Check all rows
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != '.':
                    row.append(board[i][j])
            if has_duplicates(row):
                return False

        # Check all columns
        for i in range(9):
            column = []
            for j in range(9):
                if board[j][i] != '.':
                    column.append(board[j][i])
            if has_duplicates(column):
                return False

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


