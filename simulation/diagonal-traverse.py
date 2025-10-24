class Solution(object):
    def findDiagonalOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        diagonal_map = defaultdict(list)
        res = []
        
        for r in range(rows):
            for c in range(cols):
                diagonal_map[r + c].append(matrix[r][c])
                
        for key, valueList in diagonal_map.items():
            if key % 2 == 0:
                res.extend(valueList[::-1])
            else:
                res.extend(valueList)
        
        return res