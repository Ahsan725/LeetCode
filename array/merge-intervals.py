class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key = lambda i : i[0])
        intervals.sort()
        res = [intervals[0]]

        #intervals = [[1,4],[4,5]]

        for start, end in intervals:
            last_end_value = res[-1][1]

            if start <= last_end_value:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res

        