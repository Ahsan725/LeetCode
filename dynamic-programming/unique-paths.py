class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        def paths(i, j):

            #bas case
            if i == 0 and j == 0:
                return 0
            elif i < 0 or j < 0 or i >= m and j >= n:
                return 0
            else:
                return paths(i, j - 1)  + paths(i - 1, j)
        
        paths(m-1, n-1) #starting from the end 