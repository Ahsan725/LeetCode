class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #we are checking if nums1 the element exist in nums2 and find the elemnt that is immeidtely right to it and is greater 

        #approach: iterate over nums1 then for each num in nums1 we search the index of that same element in nums2
        #we have to consider the index + 1 to it and see if that is greater than the cur element
        #if it is we append that num to the res, otherwise we append -1 
        #we also append -1 if it is the last element

        #O(n) * m (len of nums1)

        #Input: nums1 = [2,4], nums2 = [1,2,2,4]
        # 1 -> 1 + 1 -> 2
        #res [3, -1]

        #iterate over num1
        #Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
        res = [] #[-1,3, -1]

        for num in nums1: #4
            index = nums2.index(num) #index of the cur element look for 4 in nums2 return 2
            nxt_index = index + 1 #4
            if nxt_index < len(nums2) and nums2[nxt_index] > num:
                res.append(nums2[nxt_index])
            else:
                res.append(-1)

        return res 
                


