class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Count the frequency of each character
        freq = Counter(word)
        
        # Iterate through each character in the word
        for char in freq:
            # Decrease the frequency of the current character by 1
            freq[char] -= 1
            # If the frequency becomes 0, remove the character from the dictionary
            if freq[char] == 0:
                del freq[char]
            
            # Check if all remaining frequencies are equal
            unique_freq = set(freq.values())
            if len(unique_freq) == 1:
                return True
            
            # Restore the frequency of the current character
            freq[char] += 1
        
        return False