class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtrack():
            for c in count:
                if count[c] >:
                    count[c] -= 1
                    res += 1
                    res += backtrack()
                    count[c] += 1
            return res 

        return backtrack()
