class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        overlaps = 1
        intervals.sort()

        for i in range(1, len(intervals)):
            #if the start is less than the end there is an overlap
            start, end = intervals[i]
            prevstart = intervals[i-1][0] 
            prevend = intervals[i-1][1]
            if start <= prevend:
                overlaps += 1
            


        return overlaps