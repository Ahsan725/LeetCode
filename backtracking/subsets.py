class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res_set = set()
        res.append([])
        res.append(nums)

        for num in nums:
            res.append([num])

        for i in range(0, len(nums) - 1):
            for j in range(1, len(nums)):
                if nums[i] != nums[j]:
                    temp = []
                    temp = [nums[i], nums[j]]
                    res.append(temp)

        return res