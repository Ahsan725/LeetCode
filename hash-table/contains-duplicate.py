class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set()

        for num in nums:
            distinct.add(num)
        if len(distinct) == len(nums):
            return False
        else: return True