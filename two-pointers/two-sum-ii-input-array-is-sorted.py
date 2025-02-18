class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) -1
        
        while l < r:
            if numbers[l] + numbers[r] > target: 
                r -= 1 #nums too big decreas r
            elif numbers[l] + numbers[r] < target:
                l += 1 #nums too small decreas r
            else:
                return [l+1, r+1]