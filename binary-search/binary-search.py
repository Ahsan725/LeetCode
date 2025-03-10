class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) -1 

        while l < r: #l =0, r = 5
            m = (l + r) // 2 # 0 + 5 = 5 //2-> 2 + 1 = 3
            if target == nums[m]: #5 == 9?
                return m
            elif nums[m] > target: #5 > 9?
                #should reduce 
                r = m - 1 
            else:
                l = m + 1 #l = 3+ 1 = 4
        
        return -1