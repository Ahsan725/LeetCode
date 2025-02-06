class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # x = str(x)
        # return x == x[::-1] #using python built in method very useful 
        
        if x < 0: #using math concepts to extract numbers digit by digit 
            return False
        original_value = x
        reverse = 0

        while x > 0: #x = 12
            ld = x % 10 # 12 -> 2
            reverse = (reverse * 10) + ld # 12
            x = x//10 # 121/10 -> 12
        return reverse == original_value