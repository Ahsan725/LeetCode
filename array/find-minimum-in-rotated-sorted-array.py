class Solution:
    def findMin(self, nums: List[int]) -> int:
        SortedNums = sorted(nums)
        return SortedNums[0]
        