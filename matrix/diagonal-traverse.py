class Solution(object):
    def findDiagonalOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        diagonal_map = defaultdict(list)
        res = []

        #{0:1, 1:[2,4], 2:[3,5,7] 3:[6,8], 4:[9]}

        #the key part is remembering the intuition for this. That the sum of each r + c will map to a 
        #diaogonal line. Then just reverse the even diagonal sequence
        
        for r in range(rows):
            for c in range(cols):
                diagonal_map[r + c].append(matrix[r][c])
                
        for key, valueList in diagonal_map.items():
            if key % 2 == 0:
                res.extend(valueList[::-1])
            else:
                res.extend(valueList)
        return res