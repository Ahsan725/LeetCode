class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #if therre is duplicate 
        #set if not in set and nums:
        seen = set(nums)

        for i in range(len(nums)):
            if i not in seen:
                return i
        return i + 1