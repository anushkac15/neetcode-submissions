class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        mp1 = defaultdict(int)
        mp2 = defaultdict(int)

        for s in s1:
            mp1[s] += 1

        l = 0
        r = 0

        while r < len(s2):
            mp2[s2[r]] += 1

            if r - l + 1 > len(s1):
                mp2[s2[l]] -= 1

                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]

                l += 1

            if mp1 == mp2:
                return True

            r += 1

        return False
