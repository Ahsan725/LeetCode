class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        last_word = words[-1] #returns the last word in the words array;
        return len(last_word)

        