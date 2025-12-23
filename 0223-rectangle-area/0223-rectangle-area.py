class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        over_lap = 0
        
        if not (ax1 <= bx1 <= ax2 or bx1 <= ax1 <= bx2) or not (ay1 <= by1 <= ay2 or by1 <= ay1 <= by2):
            over_lap = 0
        else:
            xi,xf = max(ax1,bx1),min(ax2,bx2)
            yi,yf = max(ay1,by1),min(ay2,by2)
            over_lap = (xf-xi)*(yf-yi)
        
        area1 = (ax2-ax1)*(ay2-ay1)
        area2 = (bx2-bx1)*(by2-by1)
        
        return area1+area2-over_lap
