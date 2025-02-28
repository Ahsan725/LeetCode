class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for i in range(len(s)-1):
            summ = abs(ord(s[i]) - ord(s[i+1]))
            res += summ
        return res