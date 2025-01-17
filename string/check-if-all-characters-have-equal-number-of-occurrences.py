class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        #create a map 

        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        set_freq = freq[s[0]]

        for key, value in freq.items():
            if value != set_freq:
                return False
        
        return True