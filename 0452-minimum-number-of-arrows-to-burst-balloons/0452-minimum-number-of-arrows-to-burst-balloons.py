class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        start,end = points[0][0],points[0][1]

        for r in range(len(points)):
            if not start <= points[r][0] <= end:
                res+=1
                start,end = points[r][0],points[r][1]
            else:
                start,end = max(start,points[r][0]), min(end,points[r][1])
        return res