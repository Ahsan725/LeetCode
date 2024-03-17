class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle: 
        #splice a substring starting at index i to the length of needle so
        #if needle was 3 letters It will splice a 3 letter substring starting
        #at index i, which will them be matched with the word we are looking for
                return i
        return -1
