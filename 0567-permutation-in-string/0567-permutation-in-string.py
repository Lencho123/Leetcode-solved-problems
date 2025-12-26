class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        window = defaultdict(int)
        
        l = 0 
        for r in range(len(s2)):
            window[s2[r]]+=1
            
            while window[s2[r]] > c1[s2[r]]:
                window[s2[l]]-=1
                l+=1
            
            if r-l+1 < len(s1):
                continue
            
            if r-l+1 == len(s1):
                return True
        return False
            