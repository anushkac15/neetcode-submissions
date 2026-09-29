class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)
        l = 1
        r = max(piles)

        def canEat(piles, mid, h):
            actualHours = 0
            for pile in piles:
                actualHours += pile // mid

                if pile % mid != 0:
                    actualHours += 1

            return actualHours <= h

        while l < r:
            mid = l + (r - l) // 2

            if canEat(piles, mid, h):
                r = mid
            else:
                l = mid + 1

        return l
