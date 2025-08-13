class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and abs(nums[i] - nums[j]) == k:
                    if (nums[i], nums[j]) in pairs or (nums[j], nums[i]) in pairs:
                        continue
                    else:
                        pairs.add((nums[i], nums[j]))
            print(pairs)

        return len(pairs)
