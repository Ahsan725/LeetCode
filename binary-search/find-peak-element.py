from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Initialize left and right pointers
        l = 0
        r = len(nums) - 1

        while l < r:  # Continue until left meets right
            m = (l + r) // 2  # Find the middle index
            
            # Compare middle element with the right neighbor
            if nums[m] < nums[m + 1]:  
                l = m + 1  # Move right if the right neighbor is greater
            else:
                r = m  # Move left otherwise

        # At the end of the loop, l == r, which points to a peak element
        return l  # Return the index of the peak
