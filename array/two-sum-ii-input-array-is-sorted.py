class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                #too big reduce r 
                r -= 1
            elif total < target:
                #too small increase l
                l += 1
            else:
                return [l+1, r+1]
        return []
