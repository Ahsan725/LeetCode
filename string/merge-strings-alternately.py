class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n = len(word1)
        m = len(word2)
        res = []
        curr = 0

        for i in range(n):
            res.append(word1[i])
            curr = i
            if i in range(m):
                res.append(word2[i])

        if m > n:
            for i in range(curr + 1, m):
                res.append(word2[i])
        if n > m:
            for i in range(curr + 1, n):
                res.append(word1[i])

        res = "".join(res)
        return res 

            
        