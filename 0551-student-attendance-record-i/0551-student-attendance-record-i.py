class Solution:
    def checkRecord(self, s: str) -> bool:
        count = Counter(s)
        if count["A"] > 1:
            return False
        
        for i in range(2, len(s)):
            if s[i-2:i+1] == "LLL":
                return False
        return True