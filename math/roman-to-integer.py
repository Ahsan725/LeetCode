class Solution:
    def romanToInt(self, s: str) -> int:
        
        #Input: s = "MCMXCIV" -> 1000 + 100 - 1000 + 10 - 100
        #if you see a big value add it, if you see a smaller value followed by a big value subtract small from big
        # Output: 1994 
        #hashmap = {k:M -> 1000}    if map[char] > map[char +1]

        roman = {"M": 1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1, "IV": 4, "XL":40, "CD":400, "CM":900, "IX":9, "XC":90}
        #MC -> M CM -> 900
        res = 0 #58
        i = 0
        while i < len(s):
            mapping = s[i:2]
            if mapping in roman:
                res += roman[mapping]
                i + 2
            else:
                mapping = s[i]
                res += roman[mapping]
                i += 1
        return res 

