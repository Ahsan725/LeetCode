class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        This might be a better approach in an interview because it has less code and less chances to
        mess up. However, two pointer technique is something that will come in handy in many situations
        Sol 1 = O(n^3)
        Sol 2 = O(n^2) + O(n log n) -> O(n^2)
        '''
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

        res = [] # since we have to return an list of list
        nums.sort() #this is super imp. We want to sort it so our two pointer solution can work 

        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index -1]: #this means if i is on second iteration, and the previous valus is same
                continue #skip this iteration of i and move i to next place
            
            l = index + 1 #since i is fkixed, left pointer is intialized right after i
            r = len(nums) - 1 # right pointer starts at the end of the list

            while l < r:
                threesum = nums[index] + nums[l] + nums[r] #calculate threesum
                if threesum < 0: #if threesome is less than 0 which is our target value, move l forward so value gets bigger
                    l += 1
                elif threesum > 0: #if threesum too big move the r to the left so our value becomes smaller
                    r -= 1
                else: # this means the threesum is equal to 0 which is ou \r target value 
                    res.append([nums[index], nums[l], nums[r]]) #add it to the result 
                    l += 1 #update the left pointer to explore more combinations
                    while l < r and nums[l] == nums[l-1]: #keep moving l until l falls on a value that is different
                        l+= 1
        return res