class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l = 0 
        count = defaultdict(int)
        sub_count = defaultdict(int)
        res = 0
        for r in range(len(s)):
            count[s[r]]+=1
            maxLen = len(count)
            while l <= r and  maxLen > maxLetters or r-l+1 > maxSize:
                count[s[l]]-=1
                if count[s[l]] == 0:
                    del count[s[l]]
                    maxLen-=1
                l+=1
            while minSize <= r-l+1 <= maxSize:
                sub_count[s[l:r+1]]+=1
                count[s[l]]-=1
                if count[s[l]] == 0:
                    del count[s[l]]
                l+=1            
        return max(list(sub_count.values())) if list(sub_count.values()) else 0