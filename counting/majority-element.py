class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sorted_nums = sorted(nums) -> this one returns a new sorted list 
        nums.sort() # -> this one sorts the same list 
        return nums[(len(nums)//2)]