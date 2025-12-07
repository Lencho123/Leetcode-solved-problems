class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        dp = {}

        def devide_conquer(start,end):
            if end - start < 2:
                return 0
            if (start,end) in dp:
                return dp[(start,end)]
            res = float("inf")
            for i in range(start+1, end):
                left = devide_conquer(start,i)
                right = devide_conquer(i,end)
                res = min(res, values[start]*values[end]*values[i] + left + right)
            
            dp[(start,end)] = res
            return dp[(start,end)]
        
        return devide_conquer(0,len(values)-1)