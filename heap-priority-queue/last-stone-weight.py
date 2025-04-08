class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones)) #will always be bigger
            second = abs(heapq.heappop(stones))

            if first > second:
                val = first - second
                val = val * -1
                heapq.heappush(stones, val)
            
        stones.append(0)
        return abs(stones[0])

