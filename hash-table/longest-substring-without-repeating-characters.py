class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #understanding: we have to find substring of greatest length without repeating characters. They also have to be connected there can be no gaps
        #Approach: create a window that moves along to the right until we see some char that is already present, then we start removing from the left until that char is no longer
        #in the substring then we can add the new character and repeat the process. At every step maintain the max length of substring we ever found and return at the end
        #we can use a set that we can modify to keep track of all the chars in the string since it will give us O(1) lookup and O(1) removal 
        
        
        chars = set()
        res = 0
        #pointers to create the window
        l = 0
        
        for r in range(len(s)):
            #if we see a char already present
            if s[r] in chars:
                #it is which means we must remove from the left
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
            #if we have only seen new elemnts so far
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res 