class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] # Start with the empty set
        
        for num in nums:
            # For every existing subset, create a new one by adding 'num'
            # We use list(res) or res[:] to iterate over a copy so we can 
            # safely modify 'res' during the loop.
            for subset in list(res):
                new_subset = subset + [num]
                res.append(new_subset)
                
        return res