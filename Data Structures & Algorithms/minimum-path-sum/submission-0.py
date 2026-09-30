class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        def solve(i, j):

            if i >= len(grid) or j >= len(grid[0]):
                return float("inf")

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]

            if dp[i][j] != -1:
                return dp[i][j]

            down = solve(i + 1, j) + grid[i][j]
            right = solve(i, j + 1) + grid[i][j]

            dp[i][j] = min(right, down)
            return dp[i][j]

        dp = [[-1] * len(grid[0]) for _ in range(len(grid))]
        return solve(0, 0)
