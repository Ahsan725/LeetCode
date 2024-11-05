class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_map = {}
        char_to_index = {}
        res = []

        for index, char in enumerate(s):
            freq_map[char] = freq_map.get(char, 0) + 1
            if char not in char_to_index:
                char_to_index[char] = index 


        for char, freq in freq_map.items():
            if freq == 1:
                return s.index(char)


        # for char, freq in freq_map.items():
        #     #check if the frequency is 1
        #     if char in char_to_index and freq == 1:
        #         index = char_to_index[char] #get the index 
        #         res.append(index) #index
            

        #     #return the first one that was added to the map
        # if len(res) > 0:
        #     return res[0]
        # else:
        return -1