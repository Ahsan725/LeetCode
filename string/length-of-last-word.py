class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        #returns the last word in the words array;
        return len(words[-1])

        