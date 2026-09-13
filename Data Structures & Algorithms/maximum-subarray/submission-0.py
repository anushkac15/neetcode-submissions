class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum =0
        maxi =float('-inf')

        for n in nums:

            if sum<0:
                sum =0

            sum+=n
            maxi = max(maxi, sum)

        return maxi
        