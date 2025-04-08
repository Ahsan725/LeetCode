class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        #Declare variables
        rows = len(matrix)
        cols = len(matrix[0])
        row_flag = col_flag = False
        
        #decide which rows and cols have to be marked 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    
                    if r == 0:
                        row_flag = True
                    if c == 0:
                        col_flag = True
                    if r != 0 and c != 0:
                        matrix[0][c] = 0 #first row and current col index
                        matrix[r][0] = 0 #current row index and first col
        
        #mark the zeroes in the matrix as long as they are not in first row or first col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        #mark the first rows and first cols 0 if applicable 
        if row_flag:
            matrix[0] = [0] * cols
        if col_flag:
            for r in range(rows):
                matrix[r][0] = 0