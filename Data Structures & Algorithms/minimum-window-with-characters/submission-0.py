class Solution:
    def minWindow(self, s: str, t: str) -> str:

        mp = defaultdict(int)

        for ch in t:
            mp[ch] += 1

        l = 0
        r = 0
        minStart = 0
        minLen = float("inf")
        cnt = len(t)

        while r < len(s):
            charR = s[r]

            if mp[charR] > 0:
                cnt -= 1

            mp[charR] -= 1

            while cnt == 0:
                if minLen > r - l + 1:
                    minLen = r - l + 1
                    minStart = l

                mp[s[l]] += 1

                if mp[s[l]] > 0:
                    cnt += 1

                l += 1

            r += 1

        return "" if minLen == float("inf") else s[minStart : minStart + minLen]
