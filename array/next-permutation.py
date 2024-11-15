class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to the next lexicographical permutation.
        If no next permutation exists, rearrange nums to the lowest order.
        """
        n = len(nums)
        
        # Step 1: Find the break point (the first number from the end that is smaller than its next number).
        ind = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break
        
        # Step 2: If no break point exists, reverse the whole array to get the lowest permutation.
        if ind == -1:
            nums.reverse()
            return
        
        # Step 3: Find the next greater element from the end to swap with nums[ind].
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
        
        # Step 4: Reverse the subarray to the right of the break point to get the next permutation.
        nums[ind + 1:] = reversed(nums[ind + 1:])
