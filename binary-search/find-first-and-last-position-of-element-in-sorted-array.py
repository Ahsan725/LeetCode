from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the leftmost or rightmost position of the target
        def binary_search(left: bool) -> int:
            l, r = 0, len(nums) - 1
            pos = -1  # Default position if target is not found
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    pos = m  # Update position
                    if left:
                        r = m - 1  # Narrow to the left side
                    else:
                        l = m + 1  # Narrow to the right side
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return pos
        
        # Find the first and last position
        start = binary_search(left=True)
        end = binary_search(left=False)
        return [start, end]
