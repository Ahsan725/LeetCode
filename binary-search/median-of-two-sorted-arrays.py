class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure `A` is the smaller array for optimized binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A, B = nums1, nums2
        l, r = 0, len(A) - 1 

        while True:
            m = (l + r) // 2  # Midpoint of A
            j = half - m - 2  # Corresponding partition index in B

            # Get left and right elements from both arrays
            aleft = A[m] if m >= 0 else float("-infinity")
            aright = A[m + 1] if (m + 1) < len(A) else float("infinity")
            bleft = B[j] if j >= 0 else float("-infinity")
            bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Found correct partition
            if aleft <= bright and bleft <= aright:
                # If total length is odd, return min of right half
                if total % 2 == 1:
                    return min(aright, bright)
                # If even, return average of max left half & min right half
                return (max(aleft, bleft) + min(aright, bright)) / 2

            # If partition is incorrect, adjust binary search
            elif aleft > bright:
                r = m - 1  # Move left
            else:
                l = m + 1  # Move right