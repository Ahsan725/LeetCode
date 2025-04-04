from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We're going to use Binary Search.
        # This only works efficiently if the list is sorted (which it is!)

        # Step 1: Set two pointers to represent the left and right ends of the array.
        l = 0                      # 'l' stands for the left index, starting at 0 (beginning of the list)
        r = len(nums) - 1         # 'r' is the right index, starting at the last element's index

        # Step 2: Keep searching as long as the left pointer doesn't pass the right one.
        while l <= r:
            # Step 3: Find the middle index between l and r
            # This is where we "guess" the target might be.
            m = (l + r) // 2       # '//' is floor division. It gives us the middle index.
                                   # For example, if l = 0 and r = 5 → m = (0 + 5) // 2 = 2

            # Step 4: Check if the middle element is equal to the target
            if nums[m] == target:
                # \U0001f3af We found the target! Return its index
                return m

            # Step 5: If the middle element is greater than the target
            elif nums[m] > target:
                # ❌ Target must be in the *left* half (since the array is sorted)
                # So we move the right pointer to just before the middle
                r = m - 1

            else:
                # Step 6: If the middle element is less than the target
                # ❌ Target must be in the *right* half
                # So we move the left pointer to just after the middle
                l = m + 1

        # Step 7: If we exit the loop, that means the target was not found
        return -1
