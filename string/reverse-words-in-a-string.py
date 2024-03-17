class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() #splits the words on space so we should have: the sky is blue

        result = ""

        for i in range(len(words)-1, -1, -1):
            if i == len(words)-1:
                result += "" + words[i]
            else:
                result += " " + words[i]

        return result
        