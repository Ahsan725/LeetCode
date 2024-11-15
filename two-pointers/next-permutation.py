class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #if there is an array that can be made greater by changing the order of one of the numbers do that
        #else add more numbers from the left side and see if now it is possible 
        #if the number added from the left is also bigger like 5312
        #take another one 
        #once you fidn a smller number replace that with next bigger number #35312 -> 53312 -> 51233
        #if not possible then just sort it

        dup = nums
        n = len(nums) # 3-1 -> 2

        #[1,2,3] -> [1.3.2]

        for i in range(n - 1, -1, -1):
            #starting at the back of the array start comaparing elements 
            if nums[i] < nums[i + 1]:
                second = nums[i + 1]
                first = nums[i]
                nums[i] = second
                nums[i + 1] = first
        



