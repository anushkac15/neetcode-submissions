class Solution:
    def leastInterval(self, tasks: List[str], p: int) -> int:

        n = len(tasks)

        if p == 0:
            return n

        counter = [0] * 26

        for ch in tasks:
            counter[ord(ch) - ord('A')] += 1

        counter.sort()

        chunks = counter[25] - 1
        idleSpots = chunks * p

        for i in range(24, -1, -1):
            idleSpots -= min(chunks, counter[i])

        if idleSpots > 0:
            return n + idleSpots

        return n