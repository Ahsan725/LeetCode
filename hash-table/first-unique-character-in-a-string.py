class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_map = {}

        for index, char in enumerate(s):
            freq_map[char] = freq_map.get(char, 0) + 1

        for char, freq in freq_map.items():
            if freq == 1:
                return s.index(char)
        return -1