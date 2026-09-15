class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        maxlen = 0
        maxFreq = 0
        dict = defaultdict(int)

        for r in range(len(s)):
            dict[s[r]] += 1
            maxFreq = max(maxFreq, dict[s[r]])

            while (r - l + 1) - maxFreq > k:
                dict[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)

        return maxlen
