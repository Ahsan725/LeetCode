class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()

        i = 0
        while i < len(s):
            starting_i = i
            res = []
            seq = ""
            winsize = i + 10
            while i < winsize and i <len(s):
                res.append(s[i])
                i += 1
            seq = "".join(res)
            if seq in seen:
                ans.add(seq)
            else:
                seen.add(seq)
            i = starting_i + 1
        return list(ans)     