class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1] * len(nums)
        suff = [1] * len(nums)

        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        for i in range(len(ans)):
            ans[i] = pre[i] * suff[i]

        return ans
