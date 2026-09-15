class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = float("inf")
        profit = 0

        for i in range(len(prices)):
            if mini > prices[i]:
                mini = prices[i]
            else:
                profit = max(profit, prices[i] - mini)
        return profit
