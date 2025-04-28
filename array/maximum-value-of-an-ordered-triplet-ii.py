class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        prefixmax = nums[0]
        maxdiff = 0

        for k in range(1, len(nums)):
            res = max(res, maxdiff * nums[k])
            maxdiff = max(maxdiff, prefixmax - nums[k])
            prefixmax = max(prefixmax, nums[k])

            
        return res