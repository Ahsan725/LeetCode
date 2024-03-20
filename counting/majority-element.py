class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # sorted_nums = sorted(nums) -> this one returns a new sorted list 
        # nums.sort() # -> this one sorts the same list 
        # return nums[(len(nums)//2)] 


        candidate = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count +=1
            elif nums[i] == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
