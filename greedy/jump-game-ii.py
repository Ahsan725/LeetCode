class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_bound = 0
        max_reach = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == curr_bound:
                jumps += 1
                curr_bound = max_reach

        return jumps
