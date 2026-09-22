class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = defaultdict(int)
        maxFreq = 0

        for t in tasks:
            freq[t] += 1
            maxFreq = max(maxFreq, freq[t])

        maxCount = 0

        for f in freq.values():
            if f == maxFreq:
                maxCount += 1

        space = maxFreq - 1
        idleSlots = space * (n + 1) + maxCount

        return max(len(tasks), idleSlots)
