class Solution:
    def longestPalindrome(self, s: str) -> str:

        def solve(i, j, dp):

            if i>=j:
                return 1

            if dp[i][j] !=-1:
                return dp[i][j]

            if s[i] == s[j] and solve(i+1, j-1, dp):
                dp[i][j] = 1
            else:
                dp[i][j] = 0

            return dp[i][j]==1

        start =0
        maxlen = 1

        dp = [[-1]*len(s) for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i,len(s)):

                if solve(i, j, dp) and (j-i+1) >maxlen:
                    start =i
                    maxlen = max(maxlen, j-i+1)

        return s[start: start+maxlen]


        
        