class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        # Iterate over the smaller dict for efficiency
        if len(self.data) > len(vec.data):
            return vec.dotProduct(self)

        result = 0
        for i, val in self.data.items():
            if i in vec.data:
                result += val * vec.data[i]
        return result
