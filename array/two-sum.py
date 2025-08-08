class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} #num:index
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            else:
                num_map[nums[i]] = i