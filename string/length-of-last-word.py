class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split() #splits on space by default
        return len(words[-1]) #words[-1] this gives you last elements in the array words[-2]->2nd last

        