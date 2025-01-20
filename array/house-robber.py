class Solution:
    def rob(self, nums: List[int]) -> int:
        #two edge cases
        n = len(nums)

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):
            prev, curr = curr, max(curr, nums[i]+ prev)

        return curr