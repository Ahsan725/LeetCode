class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min_price to the price of the first day
        min_price = prices[0] 
        
        # Initialize max_profit to 0
        max_profit = 0
    
        # Iterate through each price in the prices array
        for price in prices:
            # Update min_price if the current price is lower than min_price
            if min_price > price:
                min_price = price
            
# Update max_profit if the profit obtained by selling at the current price
# (current price - min_price) is greater than the current max_profit
            if max_profit < price - min_price:
                max_profit = price - min_price
        
        # Return the maximum profit obtained
        return max_profit
