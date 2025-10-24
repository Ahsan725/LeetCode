class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        set up a frequency map -> then divide the frequency by n to get a freq percentage see if that is more than. n/3 if yes add
        """

        res = []
        n = len(nums)
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, frequ in freq.items():
            if frequ > (n/3):
                res.append(num)
        return res

