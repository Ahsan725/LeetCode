class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize two pointers, left and right, to the start and end of the array
        left = 0
        right = len(nums) - 1
        
        # While the search space is valid (left pointer is not greater than right)
        while left < right:
            # Find the middle index between left and right
            mid = (left + right) // 2
            
            # If the element at mid is greater than the element at right,
            # it means the smallest value is to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1  # Move the left pointer to mid + 1
                
            # If the element at mid is less than or equal to the element at right,
            # it means the smallest value is at mid or to the left of mid
            else:
                right = mid  # Move the right pointer to mid
        
        # After the loop, left will point to the smallest value
        return nums[left]  # Return the minimum element found

        