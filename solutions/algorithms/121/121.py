class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1 : return 0

        # Initialization
        n = len(prices)
        min = prices[0]
        profit = 0

        # Loop
        for i in range(n) :
            if prices[i] < min : min = prices[i]

            temp = prices[i] - min
            if temp > profit : profit = temp

        return profit