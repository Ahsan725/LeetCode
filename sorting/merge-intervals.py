class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #first thing about interval based problems is seeing if sorting will help us figure our the solution 
        res = []
        intervals.sort() #no need to do the extra lambda because it does the first val by default 
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            prevend = res[-1][1] #get the last entry and its end value 
            
            if start <= prevend:
                res[-1][1] = max(prevend, end)
            else:
                res.append([start, end])
        return res 