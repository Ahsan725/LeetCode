class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged = sorted(merged)

        total = len(merged)

        #if it is odd
        if total % 2  == 1:
            return float(merged[total // 2])
        else:
            mid1 = merged[total // 2 - 1]
            mid2 = merged[total // 2]
            return float(mid1 + mid2) / 2.0