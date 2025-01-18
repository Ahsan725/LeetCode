class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort the intervals using the start time 
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        # intervals.sort()
        res = 0
        prev_end_time = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end_time:
                prev_end_time = end 
            else:
                res += 1
                prev_end_time = min(prev_end_time, end)
        
        return res 

