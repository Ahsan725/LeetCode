class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur_words))
                return
        
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in wordDict:
                    cur_words.append(word)
                    backtrack(j+1)
                    cur_words.pop()

        
        cur_words = []
        res = []
        backtrack(0)
        return res 
