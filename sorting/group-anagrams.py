class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #O(n) solution
        def wordToKey(word): 
            wordArray = [0] * 26
            
            for i in range(len(word)):
                index = ord(word[i]) - ord('a')
                wordArray[index] += 1

            return ''.join(str(wordArray))

        mapAnagram = {}
    
        for i in range(len(strs)):
            anagramKey = wordToKey(strs[i])
            if anagramKey in mapAnagram: 
                mapAnagram[anagramKey].append(strs[i])
            else:
                mapAnagram[anagramKey] = [strs[i]]
                
        return list(mapAnagram.values())
