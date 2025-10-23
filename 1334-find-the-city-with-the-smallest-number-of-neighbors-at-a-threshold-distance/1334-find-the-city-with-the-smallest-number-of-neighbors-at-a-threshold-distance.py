class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Usin floyd warshal algorithm let me find distance of each city to each other
        dp = [[float("inf")]*n  for i in range(n)]
        
        for u,v,w in edges:
            dp[u][v],dp[v][u] = w,w

        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = 0
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][via] + dp[via][j])
                
        # check number of nei with < thereshold distance
        res = 0
        prev_count = float("inf")
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dp[i][j] <= distanceThreshold:
                    count+=1
                
            if prev_count >= count:
                res = i
                prev_count = count
        return res