class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return heap[0]
        
        
        
        # if k > 500: #for super large ks since in the worst case the algo below will be N^2 but N in average case. 
        #     nums.sort()
        #     return nums[-k]

        # k = len(nums) - k
        
        # def quickselect(l,r):
            
        #     pivot = nums[r]
        #     p = l

        #     #nums = [3,2,1,5,6,4]
        #     #.      ip         v
        #     for i in range(l, r):
        #         if nums[i] < pivot:
        #             #swap
        #             nums[i] , nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p]

        #     if k < p:
        #         return quickselect(l,p -1)
        #     elif k > p:
        #         return quickselect(p + 1, r)
        #     else:
        #         return nums[p]
        # return quickselect(0,len(nums)-1)
        