class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_result = 0
        for num in nums:
            xor_result ^= num  # XOR each element with xor_result
        return xor_result

        

        