class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.res = 0
        count = Counter(tiles)

        def backtrack():
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    self.res += 1
                    self.res += backtrack()
                    count[c] += 1
            return self.res 

        return backtrack()
