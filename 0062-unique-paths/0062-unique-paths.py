class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # TOP DOWN APPROACH
        # dp = {}
        # def dfs(i,j):
        #     if i==m-1 or j == n-1:
        #         return 1

        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     dp[(i,j)] = dfs(i,j+1) + dfs(i+1,j) 
            
        #     return dp[(i,j)]

        # return dfs(0,0)

        # ----BUTTOM UP APPROACH----- #
        dp =[[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i+1][j+1] = 1
                else:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        
        return dp[m][n]


        