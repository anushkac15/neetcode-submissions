class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        best = max(nums)
        if best <= 0:
            return best

        maxi = float("-inf")
        maxSum = 0

        for s in nums:
            maxSum += s
            if maxSum < 0:
                maxSum = 0

            maxi = max(maxi, maxSum)

        mini = float("inf")
        minSum = 0

        for s in nums:
            minSum += s

            if minSum > 0:
                minSum = 0

            mini = min(mini, minSum)

        return max(maxi, sum(nums) - mini)
