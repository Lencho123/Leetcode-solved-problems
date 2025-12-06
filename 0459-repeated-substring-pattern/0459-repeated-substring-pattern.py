class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        def help(ind):
            for r in range(0,len(s),ind):
                if s[:ind] != s[r:r+ind]:
                    return False
            return True
        
        i = 1
        while i <= len(s)//2:
            if not len(s)%i:
                if help(i):
                    return True
            i+=1
        return False
            