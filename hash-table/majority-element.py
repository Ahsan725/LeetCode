class Solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #hashmap 
        freq = {}
        max_freq = float('-inf')
        max_num = 0
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        #return the highest freq
        for num, value in freq.items():
            if value > max_freq:
                max_freq = value
                max_num = num
                
        return max_num
