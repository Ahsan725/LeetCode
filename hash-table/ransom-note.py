class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Create Counter objects for the ransomNote and magazine strings
        # note, mag = Counter(ransomNote), Counter(magazine)
        note = {}
        mag = {}

        for c in ransomNote:
            note[c] = note.get(c,0) +1
        for c in magazine:
            mag[c] = mag.get(c,0) +1
        
        # Check if the intersection of note and mag Counter objects is equal to note Counter object
        # If it is, it means that all the letters in ransomNote can be formed using the letters in magazine
        for key, value in note.items():
            if key not in mag or mag[key] < value:
                return False
        return True