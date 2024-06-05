class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #need a hashmap 
        newmap = {}
        #need a result variable 
        result = 0
        #left pointer
        l = 0
        #max frequency variable 
        maxfreq = 0

        for r in range(len(s)):
            #s[r] will return the character at index 0 in the string s first then ++ so A
            newmap[s[r]] = newmap.get(s[r], 0) + 1
            #generate a frequenecy map
            maxfreq = max(maxfreq, newmap[s[r]])

            while (r - l + 1) - maxfreq > k:
                newmap[s[l]] -= 1
                l += 1
            result = max(result, r-l + 1)
        return result
