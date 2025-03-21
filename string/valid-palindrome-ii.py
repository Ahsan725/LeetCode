class Solution(object):
    def validPalindrome(self, s):
        def verify(s, left, right, counter=0):
            n = 1
            
            while left < right :
                if s[left] != s[right]:
                    if counter < n: #you still have some substitutions allowed
                        return verify(s, left + 1, right, counter + 1) or verify (s, left, right - 1, counter + 1)
                    else:
                        return False
    
                else:
                    left += 1
                    right -=1 
            return True

        return verify(s, 0, len(s) -1)

        

