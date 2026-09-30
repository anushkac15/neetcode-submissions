class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        def solve(i, j):
            if i == len(obstacleGrid) or j == len(obstacleGrid[0]):
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                return 1


            if dp[i][j] != -1:
                return dp[i][j]

            right = solve(i, j + 1)
            down = solve(i + 1, j)

            dp[i][j] = right + down

            return dp[i][j]

        dp = [[-1] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        return solve(0, 0)
