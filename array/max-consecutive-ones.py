class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_ones = 0
        max_ones = 0
        for num in nums:
            if num == 0:
            #when we find a zero and consecutive property is broken
                count_ones = 0
            else:
                count_ones += 1
                max_ones = max(max_ones, count_ones)
        return max_ones