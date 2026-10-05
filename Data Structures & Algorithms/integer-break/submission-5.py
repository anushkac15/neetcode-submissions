class Solution:
    def integerBreak(self, n: int) -> int:

        dp = {}

        def solve(i, remaining, count):

            if remaining == 0:
                if count >= 2:
                    return 1
                return float('-inf')

            if i > remaining:
                return float('-inf')

            if (i, remaining, count) in dp:
                return dp[(i, remaining, count)]

            # skip
            skip = solve(i + 1, remaining, count)

            # take
            take = i * solve(i, remaining - i, count + 1)

            dp[(i, remaining, count)] = max(take, skip)

            return dp[(i, remaining, count)]

        return solve(1, n, 0)