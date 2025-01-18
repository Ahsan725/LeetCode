class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict) 

        def backtrack(i):
            if i == len(s): #you iterate over whatever you are using to build the decision tree for instance here the tree wasnt being build by 
            #adding or not adding a word so we dont need worddict for this. we are using string s if each character should be added or not. 
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
