class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #approach: Cretaing a hash map. iterate over it. For each element find its complement
        #if complmenet is found return tnose two indices

        mymap = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in mymap:
                return [mymap[comp],i]
            else:
                mymap[nums[i]] = i
            