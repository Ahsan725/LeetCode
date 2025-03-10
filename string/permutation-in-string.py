class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if s1 in s2:
            return True
        elif s1[::-1] in s2:
            return True
        else: 
            return False 