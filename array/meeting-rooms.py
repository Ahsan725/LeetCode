class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #[[0,30],[5,10],[15,20]]
        #if we sort by start
        # [[7,10],[2,4]] -> [2,4] [7,10]

        intervals.sort(key=lambda x : x)
        print(intervals)

        for i in range(1, len(intervals)):
            start = intervals[i -1][0]
            end = intervals[i - 1][1]

            newstart = intervals[i][0]
            newend = intervals[i][0]

            if newstart < end:
                return False
        
        return True
                



            