class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #keep track of all elements that are in the subarray 
        chars = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in chars:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
            chars.add(s[r])
            res = max(res, r-l + 1)
        return res 
    