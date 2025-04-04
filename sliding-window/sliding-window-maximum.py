class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        prevMax = float('-inf')

        l = 0
        r = k - 1 

        while r < len(nums):
            for i in range(l, r+1):
                prevMax = max(prevMax, nums[i])
            res.append(prevMax)
            prevMax = float('-inf')
            l += 1
            r += 1
        return res  