class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        t = rows * cols
        l = 0
        r = t -1 
        
        while l <= r:
            mid = (l + r) // 2
            #the observation below is the key to solving
            i = mid // cols
            j = mid % cols
            
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1 
                
        return False
        