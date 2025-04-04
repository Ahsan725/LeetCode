from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for i in range(len(nums)):

            # Maintain a decreasing deque: remove indices whose values are less than the current value
            # These elements can never be the max if nums[i] is larger
            while q and nums[q[-1]] < nums[i]:
                q.pop()  # Remove smaller elements from the back
            q.append(i)  # Add current index to the deque

            # Remove indices that are out of the current window's left bound
            while q and q[0] < i - k + 1:
                q.popleft()  # Remove elements outside the window from the front

            # Once we've formed a full window, add the max (at the front of the deque) to the result
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
