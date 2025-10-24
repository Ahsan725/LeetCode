class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        set up a frequency map -> then divide the frequency by n to get a freq percentage see if that is more than. n/3 if yes add
        """
        # res = []
        # n = len(nums)
        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        
        # for num, frequ in freq.items():
        #     if frequ > (n/3):
        #         res.append(num)
        # return res

        """
        This is a three step process:
        - first we find the possible candidates
        - then we get the actual count of the candidates
        - then we check if they are more than n/3 
        """
        res = []
        n = len(nums)
        cand1 = cand2 = count1 = count2 = 0
        #step 1
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 += 1
            elif count2 == 0:
                cand2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
            
        #step 2
        count1, count2 = 0, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        #step 3:
        if count1 > n/3:
            res.append(cand1)
        if count2 > n/3:
            res.append(cand2)

        return res




