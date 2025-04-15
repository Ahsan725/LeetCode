class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort people based on how much more expensive City B is than City A
        # This lets us prioritize who benefits the most from going to B vs A
        # costs.sort(key=lambda cost: cost[0] - cost[1])

        # total_cost = 0
        # n = len(costs) // 2

        # # First n go to City A
        # for i in range(n):
        #     total_cost += costs[i][0]
        
        # # Last n go to City B
        # for i in range(n, 2 * n):
        #     total_cost += costs[i][1]

        # return total_cost

        diffs = []

        # Store [difference, cost to A, cost to B]
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])

        # Sort by savings if sent to city B instead of A
        diffs.sort()

        res = 0
        n = len(diffs) // 2

        for i in range(len(diffs)):
            if i < n:
                res += diffs[i][2]  # Send to city B
            else:
                res += diffs[i][1]  # Send to city A

        return res

