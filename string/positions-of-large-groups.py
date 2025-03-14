class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l = 0
        r = 0
        res =[]

        while r < len(s):
            if s[l] == s[r]:
                start = l
                while r < len(s) and s[l] == s[r]:
                    r += 1
                end = r - 1
                l = r
                if end - start >= 2:
                    res.append([start, end])
        return res