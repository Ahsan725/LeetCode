class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #one of those problems where you will have to memroize the observations because making these
        #in the interview would take much longer than allowed. The code is simple but to prove why
        #it works is what needs to be done
        
        n = len(matrix)
        # transposing the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversing each row of the matrix
        for i in range(n):
            matrix[i].reverse()