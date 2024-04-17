class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        note = {}
        mag = {}

        for c in ransomNote:
            note[c] = note.get(c,0) +1
        #this block of code does the same as a Counter object, use this.
        for c in magazine:
            mag[c] = mag.get(c,0) +1
        
        for key, value in note.items(): #returns the entries 
            if key not in mag or mag[key] < value:
                return False
        return True