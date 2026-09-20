class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        def solve(i, target):

            if target < -total or target > total:
                return 0

            if i == len(nums):
                return 1 if target == 0 else 0

            if dp[i][target + total] != -1:
                return dp[i][target + total]

            add = solve(i + 1, target - nums[i])
            sub = solve(i + 1, target + nums[i])

            dp[i][target + total] = add + sub

            return dp[i][target + total]

        dp = [[-1] * (2 * total + 1) for _ in range(len(nums))]

        return solve(0, target)