class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums) -1 
        i = 0
        max_jump = 0

        while i <= dest:
            max_jump = nums[i]
            if i + max_jump >= dest:
                return True
            i += max_jump
        
        return False
        