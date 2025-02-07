class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

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
                res.append(l+1)
                res.append(r+1)
                break
        return res
