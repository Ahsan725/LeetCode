class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #approach: Cretaing a hash map. iterate over it. For each element find its complement
        #if complmenet is found return tnose two indices
        #key -> the number
        #value -> the index
        #what we are returning -> index

        nummap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nummap:
                return [nummap[comp], i]
            else:
                nummap[nums[i]] = i
            