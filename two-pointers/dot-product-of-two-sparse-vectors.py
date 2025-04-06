class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = {}
        for i, num in enumerate(nums):
            if num:
                self.data[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        out, vec2 = 0, vec.data
        for key, val in self.data.items():
            if key in vec2:
                out+=vec2[key]*val
        return out
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)