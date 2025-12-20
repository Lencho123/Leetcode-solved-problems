class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)
        
        def split_count(cpdomain):
            freq = 0
            d1,d2,d3 = "","",""
            
            for i,char in enumerate(cpdomain):
                if char == " ":
                    freq = int(cpdomain[:i])
                    d1 = cpdomain[i+1:]
                    
                elif char == ".":
                    if not d2:
                        d2 = cpdomain[i+1:]
                    else:
                        d3 = cpdomain[i+1:]
                        
            if d1: count[d1]+=freq
            if d2: count[d2]+=freq
            if d3: count[d3]+=freq
            
        for cp in cpdomains:
            split_count(cp)
        
        res = []
        for key,val in count.items():
            res.append(str(val) + " " + key)
        return res
            