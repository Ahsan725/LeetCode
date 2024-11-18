class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Step 1: Input validation to handle edge cases (e.g., empty matrix)
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])

        # Step 2: Initialize two boolean arrays to track which rows and columns need to be zeroed
        zero_row = [False] * rows
        zero_col = [False] * cols

        # Step 3: Iterate through the matrix to mark rows and columns that contain zero
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_row[row] = True  # Mark the entire row to be zeroed
                    zero_col[col] = True  # Mark the entire column to be zeroed

        # Step 4: Iterate through the matrix again to set the appropriate cells to zero
        for row in range(rows):
            for col in range(cols):
                # If the row or column is marked, set the cell to zero
                if zero_row[row] or zero_col[col]:
                    matrix[row][col] = 0

        # Why use lists?
        # Lists can be more memory-efficient than sets for larger matrices,
        # while still providing O(1) lookup time.