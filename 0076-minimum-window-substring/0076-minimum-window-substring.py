class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        w_count = defaultdict(int)

        res = s+s
        l = 0
        for r in range(len(s)):
            w_count[s[r]]+=1
            valid = True
            for ch in t_count:
                if w_count[ch] < t_count[ch]:
                    valid = False
                    break
            while l<=r and valid:
                if len(res) > len(s[l:r+1]):
                    res = s[l:r+1]
                w_count[s[l]]-=1
                if s[l] in t_count and w_count[s[l]] < t_count[s[l]]:
                    valid = False
                l+=1
        return res if len(res) <= len(s) else ""
