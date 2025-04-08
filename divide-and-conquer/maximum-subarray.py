class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxsub to the smallest possible value so any subarray sum will be larger
        maxsub = float('-inf')
        
        # cursum will keep track of the current subarray sum as we iterate
        cursum = 0
        
        # Loop through each number in the array
        for num in nums:

            # If the current sum is negative, it won't help us — discard it and start fresh
            # This ensures we don't carry a "negative prefix" into the new subarray
            if cursum < 0:
                cursum = 0
            
            # Add the current number to cursum — either continuing the current subarray
            # or starting a new one (if we reset it above)
            cursum += num

            # Update the maxsub if the current sum is greater than the previous maximum
            maxsub = max(maxsub, cursum)
        
        # Return the largest subarray sum found
        return maxsub
