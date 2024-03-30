class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ans=set()
        # nums.sort()
        # n=len(nums)
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for k in range(j+1,n):
        #             temp=nums[i]+nums[j]+nums[k]
        #             if temp==0:
        #                 ans.add((nums[i],nums[j],nums[k]))
        # return ans

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) -1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res