from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cnt = 0
        total = 0
        mp = defaultdict(int)
        mp[0] = 1

        for num in nums:
            total += num

            if total - k in mp:
                cnt += mp[total - k]

            mp[total] += 1

        return cnt