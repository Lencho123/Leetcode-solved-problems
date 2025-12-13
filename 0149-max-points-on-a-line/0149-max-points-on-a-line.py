class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        points.sort()
        
        res = 0
        for i in range(len(points)):
            counts = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                x = (points[j][1]-points[i][1])
                y = (points[j][0] - points[i][0])
                
                slope = "vertical"
                if y != 0:
                    slope = x/y
                    
                counts[slope]+=1
            res = max(res, max([0]+list(counts.values())))
            
        return res+1
                