class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #we can not use extra space 
        #can not modify -> no sorting 

        fast = 0 
        slow = 0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
            