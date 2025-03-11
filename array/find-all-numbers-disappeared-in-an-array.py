class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        max_num = max(nums)

        res = []

        for i in range(1, max_num):
            if i not in seen:
                res.append(i)
        return res