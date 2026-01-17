class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:  
        res = 0
        for i in range(len(bottomLeft)):
            xo1,yo1 = bottomLeft[i]
            xf1,yf1 = topRight[i]
            for j in range(i+1, len(bottomLeft)):
                xo2,yo2 = bottomLeft[j]
                xf2,yf2 = topRight[j]

                # take if they have overlapping region
                if (xo1 <= xo2 <= xf1 or xo2 <= xo1 <= xf2) and (yo1 <= yo2 <= yf1 or yo2 <= yo1 <= yf2):
                    side = min(min(xf1, xf2)-max(xo1,xo2), min(yf1, yf2)-max(yo1,yo2))

                    res = max(res, side**2)
        return res