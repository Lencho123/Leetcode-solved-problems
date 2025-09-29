class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(i,j):
            if i==m-1 or j == n-1:
                return 1

            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = dfs(i,j+1) + dfs(i+1,j) 
            
            return dp[(i,j)]

        return dfs(0,0)
        