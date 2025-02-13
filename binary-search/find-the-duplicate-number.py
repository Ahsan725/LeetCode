class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #we can not use extra space 
        #can not modify -> no sorting 

        for num in nums:
            for num2 in nums:
                if num == num2:
                    return num
        return 0