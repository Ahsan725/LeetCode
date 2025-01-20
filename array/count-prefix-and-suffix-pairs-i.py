class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        #for each word check if it starts with and ends with that string
        res = 0

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    res += 1
        
        return res
