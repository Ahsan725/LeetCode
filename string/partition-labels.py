class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {} #this stores the last occurence of each letter
        for i, c in enumerate(s):
            lastindex[c] = i
        
        res = [] 
        size = 0 #this is what we will append to the res
        end = 0 #this always mainatins the max of the index of the letter that occured

        for i, c in enumerate(s):
            size += 1 #size goes up to every letter to calculate the size of parts
            end = max(end, lastindex[c]) #maintains the farthest we have to go in 1 part
            if i == end: #if current index is at 
                res.append(size)
                size = 0
        return res 
