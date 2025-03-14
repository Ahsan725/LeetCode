class Solution:
    def toGoatLatin(self, s: str) -> str:
  
        vows = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res = []
        last_char = ''
        
        words = s.split() 
        
        for i, word in enumerate(words):
            if word[0] in vows:
            #found a vowel
                res.append(word + "ma" + "a"* (i+1) )
            
            elif word[0] not in vows:
                last_char = word[0]
                res.append(word[1:] + last_char + "ma" + "a" * (i+1))
            
        return " ".join(res)
            