from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize memoization table
        n = len(coins)
        memo = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]

        def helper(coins, amount, n):
            # Base cases
            if amount == 0:  # If amount is 0, no coins are needed
                return 0
            if n == 0:  # If no coins are left and amount is not 0, impossible to solve
                return float('inf')

            # Check if the result is already computed
            if memo[n][amount] != -1:
                return memo[n][amount]

            # Choice diagram
            if coins[n - 1] <= amount:
                # Include the coin or exclude the coin
                memo[n][amount] = min(
                    1 + helper(coins, amount - coins[n - 1], n),  # Include coin
                    helper(coins, amount, n - 1)                  # Exclude coin
                )
            else:
                # Exclude the coin if its value exceeds the current amount
                memo[n][amount] = helper(coins, amount, n - 1)

            return memo[n][amount]

        # Get the result from the helper function
        result = helper(coins, amount, n)

        # If result is infinity, it means no solution exists
        return result if result != float('inf') else -1
