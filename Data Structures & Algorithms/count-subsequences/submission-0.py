class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def solve(i, j):

            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            take = 0

            if s[i] == t[j]:
                take = solve(i + 1, j + 1)

            notTake = solve(i + 1, j)

            dp[i][j] = take + notTake
            return dp[i][j]

        dp = [[-1] * len(t) for _ in range(len(s))]

        return solve(0, 0)
