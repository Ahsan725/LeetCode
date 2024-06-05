class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #this is a retry for practice use the solution before this one 

        distinct = set()

        for num in nums:
            distinct.add(num)
        
        return len(distinct) != len(nums)

        