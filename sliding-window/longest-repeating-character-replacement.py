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
            #b/w the prev maxfreq and the newly incrmntd value in the map, bigger is used
            maxfreq = max(maxfreq, newmap[s[r]])

            #this represents the number of replacements we have to make. If greater than k
            #we have to increase the left pointer
            while (r - l + 1) - maxfreq > k:
                #decrement because we are removing the first character of string from
                #consideration. Map now displays the freq of new string under consideration
                newmap[s[l]] -= 1
                #advance the l pointer to remove 
                #Now string s that will be considered will start at index 1
                l += 1
            result = max(result, r-l + 1)
        return result
