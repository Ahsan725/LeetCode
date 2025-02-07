class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balltocolor = {}
        res = []
        count = 0
        #[[0,1],[1,2],[2,2],[3,4],[4,5]]
        for ball, color in queries:
            if ball not in balltocolor and color not in balltocolor.values():
                count += 1 # 3
            res.append(count) #[1,2,3]
            balltocolor[ball] = color #map: {0:1, 1:2, 2:2,}

        return res
