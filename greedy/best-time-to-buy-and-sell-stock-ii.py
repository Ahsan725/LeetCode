class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0

        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                buy = prices[i] # 3
                sell = prices[i+1] # 6
                profit += sell - buy # 4 + 3 = 7
        return profit 

