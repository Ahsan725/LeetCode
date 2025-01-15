from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        track = Counter(word)
        
        # Iterate over a list of the keys to avoid modifying the dictionary during iteration
        for key in list(track.keys()):
            track[key] -= 1
            #if frequency become zero , delete element (to handle edge case)
            if track[key] == 0:
                del track[key]
            
            # Check if all remaining frequencies are the same
            if len(set(track.values())) == 1:
                return True

            # Restore the count for the next iteration
            track[key] += 1
        
        return False