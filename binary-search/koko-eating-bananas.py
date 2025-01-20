from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize the search boundaries
        l = 1  # Minimum possible eating speed
        r = max(piles)  # Maximum possible eating speed

        while l < r:
            m = (l + r) // 2  # Current eating speed to test

            # Calculate total hours required with eating speed m
            temp_res = 0
            for pile in piles:
                # Using math.ceil to account for partial hours
                temp_res += math.ceil(pile / m)

            if temp_res > h:
                # K is too small, need to increase it
                l = m + 1
            else:
                # K might be too large, try to find a smaller valid K
                r = m

        # At this point, l == r and is the minimum valid K
        return l
