class Solution:
    def checkValidString(self, s: str) -> bool:

        open = 0
        close = 0

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "*":
                open += 1
            else:
                open -= 1

            if s[len(s) - i - 1] == ")" or s[len(s) - i - 1] == "*":
                close += 1
            else:
                close -= 1

            if open < 0 or close < 0:
                return False

        return True
