class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        left = nums[0]
        for j in range(len(nums)):
            if nums[j] > left:
                left = nums[j]
                continue
            for k in range(j + 1, len(nums)):
                res = max(res, ((left - nums[j]) * nums[k]))
        return res 