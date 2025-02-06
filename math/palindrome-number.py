class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        #because if there is a negative sign on one side it can never be palins
        original = x
        reverse = 0 
        while x > 0:
            last = x % 10 #786 -> 6 786%10-> 780 -> 6 
            reverse = (reverse * 10) + last
            x = x // 10 # 786 // 10 -> 78
        return original == reverse 