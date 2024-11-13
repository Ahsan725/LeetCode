class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos_ptr = 0 #index 0 -> 0 + 2 -> 2
        neg_ptr = pos_ptr + 1 # index 1 -> 2+ 1-> 3
    
        for i in range(len(nums)):
            if nums[i] >= 0:
                res[pos_ptr] = nums[i]
                if pos_ptr <= len(res) - 3: 
                    pos_ptr += 2
            else:
                res[neg_ptr] = nums[i]
                if neg_ptr <= len(res) - 3: 
                    neg_ptr += 2
        return res