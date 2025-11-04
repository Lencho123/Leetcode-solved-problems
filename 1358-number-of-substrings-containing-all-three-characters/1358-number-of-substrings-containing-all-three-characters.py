class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        dct = defaultdict(int)
        l = 0

        for r in range(len(s)):
            dct[s[r]] += 1
            if  dct["a"] > 0 and dct["b"] > 0 and dct["c"] > 0:
                # take the valid substarings:
                res += len(s)-r
            while dct["a"] > 0 and dct["b"] > 0 and dct["c"] > 0:
                # shrink the window
                dct[s[l]]-=1
                l+=1
                if dct["a"] > 0 and dct["b"] > 0 and dct["c"]:
                    res+=len(s) - r
        return res