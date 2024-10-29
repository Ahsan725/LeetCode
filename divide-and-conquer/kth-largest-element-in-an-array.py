class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > 500:
            nums.sort()
            return nums[-k]

        k = len(nums) - k
        
        def quickselect(l,r):
            
            pivot = nums[r]
            p = l

            #nums = [3,2,1,5,6,4]
            #.      ip         v
            for i in range(l, r):
                if nums[i] < pivot:
                    #swap
                    nums[i] , nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                return quickselect(l,p -1)
            elif k > p:
                return quickselect(p + 1, r)
            else:
                return nums[p]
        return quickselect(0,len(nums)-1)