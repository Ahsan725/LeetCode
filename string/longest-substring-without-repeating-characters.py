'''
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew" len = 1
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

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

                    
                
            
            
            
            
            
            
            
            
            
            
            
            
            
        