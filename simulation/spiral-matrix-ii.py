class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #first row is in the original order
        #last row is in reverse order
        #the middle row is has the last element in the middle right is from the left and left is from right

        mat = [[0] * n for _ in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        val =1 

        while left <= right:

            #fill the top row
            for c in range(left, right + 1):
                mat[top][c] = val
                val+= 1
            top +=1 

            #fill the right col
            for r in range(top, bottom + 1):
                mat[r][right] = val
                val += 1
            right -= 1

            #fill the bottom row
            for c in range(right, left -1, -1):
                mat[bottom][c] = val
                val +=1 
            bottom -= 1

            #fill the left col
            for r in range(bottom, top -1, -1):
                mat[r][left] = val
                val += 1
            left += 1
        
        return mat


