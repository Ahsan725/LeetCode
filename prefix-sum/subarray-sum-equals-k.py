class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0 : 1}
        # nums = [1,2,3], k = 3
        res = 0
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i] # curr = 6 
            prev = current_sum - k # 6 - 3 = 3
            if prev in prefix_map: # yes 0 exists in map
                res += prefix_map[prev] # -> 1
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1 # map = {0:1, 1:1, 2:1, }
        return res # res = 1
        
        
        