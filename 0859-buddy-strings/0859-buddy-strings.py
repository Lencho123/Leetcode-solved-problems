class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        double = False
        cnt = Counter(s)
        for c in cnt:
            if cnt[c] >= 2:
                double = True
        
        fro_s = []
        fro_g = []
        count = 0
        for i in range(len(s)):
            
            if s[i] != goal[i]:
                fro_s.append(s[i])
                fro_g.append(goal[i])
                count+=1
            if count > 2: return False
        
        
        return (count == 2 and fro_s[0] == fro_g[1] and fro_s[1] == fro_g[0]) or count == 0 and double