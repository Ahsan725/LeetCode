

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        freq = Counter(nums)
        res = 0

        if k == 0:
            # Count numbers with duplicates
            for v in freq.values():
                if v > 1:
                    res += 1
        else:
            # Check if x + k exists for each unique x
            for x in freq:
                if x + k in freq:
                    res += 1
        
        return res
