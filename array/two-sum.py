class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in num_indices:
                return[i, num_indices[comp]]
            else:
                num_indices[nums[i]] = i
                    
                