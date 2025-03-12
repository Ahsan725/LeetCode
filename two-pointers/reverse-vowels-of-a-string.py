class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) -1
        vows = {"a","e","i","o","u","A","E","I","O","U"}
        found = []
        res = []

        for char in s:
            if char in vows:
                found.append(char)
        # found = found[::-1]

        for char in s:
            if char in vows:
                res.append(found.pop())
            else:
                res.append(char)
        return "".join(res)