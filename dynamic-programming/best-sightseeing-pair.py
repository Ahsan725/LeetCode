class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = []

        def calculate_sight(i,j):
            return values[i] + values[j] + i - j

        for i in range(len(values)-1):
            for j in range(i + 1, len(values)):
                res.append(calculate_sight(i,j))


        sorted_res = sorted(res)
        
        return sorted_res[-1]