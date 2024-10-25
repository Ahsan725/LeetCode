class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        dp = set()# set = {0, 5, }
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            newdp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                newdp.add(t + nums[i])
                newdp.add(t)
            dp = newdp
        if target in dp:
            return True
        else:
            return False
        