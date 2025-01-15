class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = {}

        for c in word:
            freq[c] = freq.get(c, 0) + 1
        
        #look at the value of each key and see if they are similar we are allowed at most 1
        #a-> 1 b->1 c-> 2
        wrd = word[0]
        starting = freq[wrd]
        char_deleted = 0

        for key, value in freq.items():
            if value != starting:
                #it different now we check if it can be fixed using one character 
                if abs(value - starting) < 2:
                    #also needs to mark that we have used up our allotment
                    char_deleted += 1
                elif char_deleted != 0:
                    return False
                else:
                    return False
        
        for key, value in freq.items():
            if value == starting and char_deleted == 0:
                return False
        
        return True 