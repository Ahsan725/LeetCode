class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #subarray, cursum 
        
        #the idea is to not include negative prefix in the sum 
        
        maxsub = float('-inf')
        cursum = 0
        
        for num in nums:
            if cursum < 0:
                cursum = 0
            
            cursum += num

            maxsub = max(maxsub, cursum)
        return maxsub