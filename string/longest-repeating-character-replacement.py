class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #need a hashmap 
        newmap = {}
        #need a result variable 
        result = 0
        l = 0
        maxfreq = 0

        for r in range(len(s)):
            newmap[s[r]] = 1 + newmap.get(s[r], 0)
            #generate a frequenecy map
            maxfreq = max(maxfreq, newmap[s[r]])

            while (r - l + 1) - maxfreq > k:
                newmap[s[l]] -= 1
                l += 1
            result = max(result, r-l + 1)
        return result
