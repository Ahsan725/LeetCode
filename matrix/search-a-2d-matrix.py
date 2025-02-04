class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #def binary searech
        #this solution treats the 2d matrix as a 1d list. it picks the middle index. This index is then converted into the cordinate of the 2d matrix
        #this is done using division by cols because what is in 2d matrix that is not present in a 1d list -> cols. 

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

    

        