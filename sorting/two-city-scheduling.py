class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort people based on how much more expensive City B is than City A
        # This lets us prioritize who benefits the most from going to B vs A
        costs.sort(key=lambda cost: cost[0] - cost[1])

        total_cost = 0
        n = len(costs) // 2

        # First n go to City A
        for i in range(n):
            total_cost += costs[i][0]
        
        # Last n go to City B
        for i in range(n, 2 * n):
            total_cost += costs[i][1]

        return total_cost
