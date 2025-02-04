class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #def binary searech

        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        l = 0
        r = total - 1 


        while l <= r:
            mid = (l+r) //2
            i = mid // cols
            j = mid % cols 

            if matrix[i][j] == target:
                return True 
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid -1 

        return False

    

        