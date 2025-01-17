class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0 #this is what we will use to count the number of palins 
        uniq = set(s) #create a set of characters in s 

        for c in uniq: 
            start = s.find(c)
            end = s.rfind(c)

            if start < end:
                res += len(set(s[start + 1: end]))
        return res

        #better than neetcode solution 