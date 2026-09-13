class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def pal(s):

            return s==s[::-1]

        def solve(i, res, temp):

            if i==len(s):
                res.append(temp[:])
                return 

            for idx in range(i+1, len(s)+1):

                sub = s[i:idx]

                if pal(sub):

                    temp.append(sub)
                    solve(idx, res, temp)
                    temp.pop()

        res = []
        solve(0, res, [])
        return res
                    
        