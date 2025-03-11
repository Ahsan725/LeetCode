class Solution:
    def countSegments(self, s: str) -> int:
        
        tokens = s.split()

        return len(tokens)