class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            res.append(num)
        
        n = len(res) # 3
        idx = len(nums) # 3 

        # for i in range(n): #0-2
        #     res[i + n] = nums[i]

        for num in nums:
            res.append(num)

        return res