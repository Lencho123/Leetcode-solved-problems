class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        c_r = list(zip(capacity,rocks))
        c_r.sort(key = lambda x: x[0]-x[1])
        res = 0

        for c,r in c_r:
            if additionalRocks >= c-r:
                res+=1
                additionalRocks -= c-r
        return res