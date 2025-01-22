class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for i in range(len(words)):
            if words[i].startswith(pref):
                res += 1
        return res