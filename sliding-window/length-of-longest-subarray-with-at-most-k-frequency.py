class Solution:
    def maxSubarrayLength(self, arr: List[int], k: int) -> int:
        freq = {}
        l = 0
        res = 0
        
        for r in range(len(arr)):
            # build mp
            freq[arr[r]] = 1 + freq.get(arr[r], 0)
            # validate window
            while freq[arr[r]] > k:
                freq[arr[l]] -= 1
                l += 1
            
            # store max 
            res = max(res, r - l + 1)
        return res