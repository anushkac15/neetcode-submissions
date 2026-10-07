class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n = min(len(word1), len(word2))
        merged = ""

        for i in range(n):
            merged += word1[i] + word2[i]

        merged += word1[n:] + word2[n:]

        return merged
