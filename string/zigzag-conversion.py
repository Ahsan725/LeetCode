class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If numRows is less than or equal to 1, no conversion is needed
        if numRows <= 1:
            return s
    
        # Initialize a list to store characters for each row
        rows = [''] * numRows
        current_row, direction = 0, 1
    
        for char in s:
            rows[current_row] += char
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction
        
        return ''.join(rows)
