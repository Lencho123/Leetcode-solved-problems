class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        if not hBars or not vBars:
            return 1

        hole = 4   
        hBars.sort()
        vBars.sort()

        h_cons = 1
        v_cons = 1

        h_cons_set = set()

        for i in range(1,len(hBars)):
            h_cons_set.add(h_cons)
            if  hBars[i] != hBars[i-1]+1:
                h_cons = 0
            
            h_cons+=1
        h_cons_set.add(h_cons)

        for i in range(1,len(vBars)):
            if v_cons in h_cons_set:
                hole = max(hole, (v_cons+1)**2)
            if  vBars[i] != vBars[i-1]+1:
                v_cons = 0

            v_cons+=1

        if v_cons in h_cons_set:
                hole = max(hole, (v_cons+1)**2)
        return hole