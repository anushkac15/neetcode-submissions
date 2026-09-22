class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target > nums[mid]:
                l += 1
            elif target < nums[mid]:
                r -= 1

            else:
                return mid
        return -1
