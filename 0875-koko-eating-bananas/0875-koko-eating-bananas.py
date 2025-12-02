class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):

            time = 0
            for p in piles:
                time+=ceil(p/speed)
            return time <= h
            

        
        l,r = 1, max(piles)

        while l <= r:
            m = l + (r-l)//2

            if feasible(m):
                r = m-1
            else:
                l = m+1
        return l
