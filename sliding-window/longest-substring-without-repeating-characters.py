
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        chars = set()

        while right < len(s):
            new_char = s[right]
            if new_char not in chars:
                chars.add(new_char)                    
                max_len = max(max_len, right - left + 1)  
                right += 1
            else:
                while s[left] != new_char:
                    chars.remove(s[left])
                    left += 1
                chars.remove(s[left])
                left += 1
        return max_len

                    
                
            
            
            
            
            
            
            
            
            
            
            
            
            
        