class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0 #this is what we will use to count the number of palins 
        uniq = set(s) #create a set of characters in s 

        for c in uniq: #ony iterate through the unqiue characters
            start = s.find(c) #use this search function to find the index of first occur of character
            end = s.rfind(c) #use this search function to find the index of last occur of character

            if start < end: #if there is elemnts between start and end
                res += len(set(s[start + 1: end])) 
                #append to res the size of the set that is created between the range of 
                #start and end of unqiue values. if start is "a" and end is "a" and the unqiue characters could be anythung
                # in between they all will be palindromes for instance "a"ghi"a" -> aga, aha, aia
        return res

        #better than neetcode solution 