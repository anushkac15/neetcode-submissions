class Solution:
    def isValid(self, s: str) -> bool:

        mp = {"]": "[", ")": "(", "}": "{"}
        st = []

        for ch in s:
            if ch in mp.values():
                st.append(ch)

            else:
                if not st or mp[ch]!=st.pop():
                    return False

        return len(st) == 0
