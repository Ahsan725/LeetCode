class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement_map = {}
        result = []
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in complement_map:
                # Found complement, return indices
                result.append(complement_map[comp])
                result.append(i + 1)
                return result
            else:
                # Store the current number's index
                complement_map[numbers[i]] = i + 1
