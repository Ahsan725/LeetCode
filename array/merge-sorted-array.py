class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res_index = len(nums1) - 1
        index_1 = m -1
        index_2 = n -1


        #nums1 = [1,2,2,3,5,6], m = 3, nums2 = [], n = 3 
        while index_1 >= 0 and index_2 >= 0:
            #start iterating from the back and start putting items that way
            if nums1[index_1] >= nums2[index_2]:
                nums1[res_index] = nums1[index_1]
                index_1 -= 1

            else:
                nums1[res_index] = nums2[index_2]
                index_2 -= 1
            
            res_index -= 1
            
        if index_2 >= 0:
            nums1[res_index] = nums2[index_2]
            res_index -= 1
            index_2 -= 1




