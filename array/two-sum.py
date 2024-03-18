class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for i in range(len(nums)):
            comp = target - nums[i] #creates a complement of the element
            if comp in num_indices: #python syntax for if the map contains comp
                return[i, num_indices[comp]]#no need for an array just return
            else: #if not seen before
                num_indices[nums[i]] = i # add it to the map
                    
                