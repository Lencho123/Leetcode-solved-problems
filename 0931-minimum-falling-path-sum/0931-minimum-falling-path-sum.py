class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[float("inf") for i in range(len(matrix[0]))] for j in range(len(matrix))]

        def dfs(i,j):
            if i == len(matrix)-1:
                return matrix[i][j]
            if dp[i][j] == float("inf"):
                dp[i][j] = matrix[i][j] + min(dfs(i+1, j), dfs(i+1,j-1) if j>0 else float("inf"), dfs(i+1,j+1) if j<len(matrix[0])-1 else float("inf"))
            return dp[i][j]
        
        res = float("inf")
        for col in range(len(matrix[0])):
            res = min(res, dfs(0,col))
        
        return res