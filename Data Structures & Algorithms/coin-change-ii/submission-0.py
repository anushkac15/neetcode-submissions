class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def solve(i, amount, dp):

            if amount == 0:
                return 1

            if amount < 0 or i == len(coins):
                return 0

            if dp[i][amount] != -1:
                return dp[i][amount]

            take = solve(i, amount - coins[i], dp)
            notTake = solve(i + 1, amount, dp)

            dp[i][amount] = take + notTake

            return dp[i][amount]

        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        return solve(0, amount, dp)
