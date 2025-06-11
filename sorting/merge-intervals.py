class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #sort the intervals 
        intervals.sort()
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            prevend = res[-1][1]
            prevstart = res[-1][0]
            
            if start <= prevend: #(1,4), (2,3) -> (1, 4)
                #overlap
                prevstart = min(prevstart, start)
                end = max(end, prevend)
                res[-1] = [prevstart, end]
                
            else:
                #do something 
                res.append([start, end])
            
        return res 
               
        