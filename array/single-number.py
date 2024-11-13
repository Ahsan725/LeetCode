class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newmap = {}
        for i in range(len(nums)):
            newmap[nums[i]] = newmap.get(nums[i], 0) + 1
        
        for key, value in newmap.items():
            if newmap[key] <= 1:
                return key
        return -1
        

        