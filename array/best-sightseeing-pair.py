class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_i = values[0] #this is the same as values[0] + 0 = values[i] + i

        for j in range(1, len(values)):
            #calculate the current score
            curr_score = max_i + values[j] - j
            max_score = max(max_score, curr_score)

            max_i = max(max_i, values[j] + j)

        return max_score