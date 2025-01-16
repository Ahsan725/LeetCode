class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = []
        biggest = -999

        def calculate_sight(i,j):
            return values[i] + values[j] + i - j

        for i in range(len(values)-1):
            for j in range(i + 1, len(values)):
                pair = calculate_sight(i,j)
                if pair > biggest:
                    biggest = pair
        
        return biggest