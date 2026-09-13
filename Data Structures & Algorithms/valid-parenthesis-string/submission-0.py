class Solution:
    def checkValidString(self, s: str) -> bool:

        openCount =0
        closeCount =0
        n = len(s)-1

        for i in range(n+1):

            if s[i] == '(' or s[i] == '*':
                openCount+=1
            else:
                openCount -=1

            if s[n-i] == ')' or s[n-i] =='*':
                closeCount +=1
            else:
                closeCount -=1

            if openCount <0 or closeCount <0:
                return False

        return True
        