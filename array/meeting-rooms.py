class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #sorting is necessary
        intervals.sort(key=lambda x : x)

        for i in range(1, len(intervals)):
            #get previous element end time
            prevend = intervals[i - 1][1]
            #get new meetings start time 
            newstart = intervals[i][0]

            if newstart < prevend:
                return False
        
        return True
                



            