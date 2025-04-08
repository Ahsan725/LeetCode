class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #use a set -> O(n) space
        #use sorting -> nlogn 

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            if value == 1:
                return key
        
