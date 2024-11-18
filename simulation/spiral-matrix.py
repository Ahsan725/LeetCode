class Solution:
    def spiralOrder(self, matrix):
        rows, cols = len(matrix), len(matrix[0])  # Total rows and columns
        current_row, current_col, direction = 0, -1, 1  # Starting position and direction
        result = []

        while rows > 0 and cols > 0:
            # Traverse horizontally
            for i in range(cols):
                current_col += direction
                result.append(matrix[current_row][current_col])
            rows -= 1

            # Traverse vertically
            for j in range(rows):
                current_row += direction
                result.append(matrix[current_row][current_col])
            cols -= 1

            # Flip direction
            direction *= -1

        return result
