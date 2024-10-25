class Solution:
    def minSteps(self, s: str, t: str) -> int:
        alphabets = [0] * 26
        res = 0
        for i in range(len(s)):
            alphabets[ord(s[i]) - ord('a')] += 1
            alphabets[ord(t[i]) - ord('a')] -= 1

        for count in alphabets:
            res += max(0, count)

        return res 
