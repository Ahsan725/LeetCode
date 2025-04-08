class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #if there is any break at any point we have to count that as seperate
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while (i+1) < len(nums) and nums[i+1] == (nums[i] + 1):
                i += 1
            end = nums[i]
            if start != end:
                ans = str(start) + "->" + str(end)
                res.append(ans)
            else:
                res.append(str(start))
            i += 1
        return res 
            

