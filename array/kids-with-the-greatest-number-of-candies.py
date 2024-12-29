class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        most_cand = max(candies)
        res = []

        for candy in candies:
            if candy + extraCandies >= most_cand:
                res.append(True)
            else:
                res.append(False)

        return res